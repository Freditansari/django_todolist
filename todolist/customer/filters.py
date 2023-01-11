import django_filters

from .models import  *

class CustomerFilter(django_filters.FilterSet):
    name =django_filters.CharFilter(field_name="name", label="Name",lookup_expr='icontains')
    company =django_filters.CharFilter(field_name="company", label="Company",lookup_expr='icontains')
    work_function =django_filters.CharFilter(field_name="work_function", label="Work Function",lookup_expr='icontains')
    phone =django_filters.CharFilter(field_name="phone", label="Phone",lookup_expr='icontains')
    email =django_filters.CharFilter(field_name="email", label="Email",lookup_expr='icontains')
    # lead_status =django_filters.CharFilter(field_name="lead_status", label="Lead Status",lookup_expr='icontains')
    # customer_category =django_filters.ChoiceFilter(field_name="customer_category", label="Customer Category")
    class Meta:
        model = Customer
        # fields ={
        #     'name': ['icontains'],
        #     'company': ['icontains'],
        #     'work_function': ['icontains'],
        #     'phone': ['icontains'],
        #     'email': ['icontains'],
        #     'lead_status': ['icontains']
        # }
        fields = '__all__'
        # fields =['name', 'company', 'work_function', 'phone', 'email']

