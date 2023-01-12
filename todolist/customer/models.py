from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Customer_Category(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.category

class Customer(models.Model):
    COLD = 'Cold'
    WARM = 'Warm'
    HOT = 'Hot'
    name = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    work_function = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    address = models.TextField(null=True, blank = True)
    notes = models.TextField(null=True, blank = True)
    estimated_sale = models.FloatField()
    lead_source = models.CharField(max_length = 512)
    lead_status_options =[
        (COLD, 'Cold'),
        (WARM, 'Warm'),
        (HOT, 'Hot'),
    ]
    lead_status = models.TextField(null=True, blank = True, choices = lead_status_options, default = WARM)
    user = models.ForeignKey(User, on_delete= models.CASCADE, null = True, blank = True, related_name='user2customer')
    customer_category = models.ForeignKey(Customer_Category, on_delete= models.CASCADE, null = True, blank = True, related_name='category2customer')
    def __str__(self):
        return self.name

class ContactLog(models.Model):
    last_contact = models.DateTimeField(default=datetime.now, blank = True)
    next_contact = models.DateTimeField()
    actions = models.TextField(null=True, blank = True)
    result = models.TextField(null=True, blank = True)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE, null = True, blank = True, related_name="user2contact")
    is_done = models.BooleanField(default = False)
    def __str__(self):
        return self.actions

class SalesLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, related_name='customer2saleslog')
    created = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default = 0)
    invoice = models.CharField(max_length = 200)
    notes = models.TextField(null=True, blank = True)
    def __str__(self):
        return self.notes