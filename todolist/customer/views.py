from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CustomerList(LoginRequiredMixin, ListView):
    model=Customer
    context_object_name = 'customers'