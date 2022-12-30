from django.contrib import admin
from .models import Customer, Contact, SalesLog
# Register your models here.

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(SalesLog)