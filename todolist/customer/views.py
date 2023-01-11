from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .filters import CustomerFilter
# Create your views here.

class CustomerList(LoginRequiredMixin, ListView):
    model=Customer
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = CustomerFilter(self.request.GET, queryset=self.get_queryset())
        return context

class CustomerCreate(LoginRequiredMixin, CreateView):
    model=Customer
    # fields = '__all__'
    fields =['name', 'company', 'work_function', 'phone', 
             'email', 'address', 'notes', 'estimated_sale',
             'lead_source', 'lead_status', 'customer_category']
    success_url = reverse_lazy('customers')
    widgets={
        
    }
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CustomerCreate, self).form_valid(form)

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model=Customer
    fields = '__all__'
    success_url = reverse_lazy('customers')
    
class DeleteView(LoginRequiredMixin, DeleteView):
    model=Customer
    fields ='__all__'
    success_url=reverse_lazy('customers')
    