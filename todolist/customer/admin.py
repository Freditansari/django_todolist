from django.contrib import admin
from .models import Customer, Contact, SalesLog, Customer_Category
# Register your models here.

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(SalesLog)
admin.site.register(Customer_Category)