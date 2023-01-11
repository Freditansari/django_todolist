import django_filters
from .models import  *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields ={
            'name': ['icontains'],
            'company': ['icontains'],
            'work_function': ['icontains'],
            'phone': ['icontains'],
            'email': ['icontains'],
            'lead_status': ['icontains']
        }
        # fields = '__all__'
        # fields =['name', 'company', 'work_function', 'phone', 'email']

