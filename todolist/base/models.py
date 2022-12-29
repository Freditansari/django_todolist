from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank = True)
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']


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
    user = models.ForeignKey(User, on_delete= models.CASCADE, null = True, blank = True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    last_contact = models.DateTimeField(auto_now_add = True)
    next_contact = models.DateTimeField()
    actions = models.TextField(null=True, blank = True)
    result = models.TextField(null=True, blank = True)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE, null = True, blank = True)