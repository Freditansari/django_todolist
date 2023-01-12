from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer, ContactLog
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .filters import CustomerFilter, ContactLogsFilter

from .forms import ContactLogForm

from datetime import date
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


class ContactLogCreate(LoginRequiredMixin, CreateView):
    model = ContactLog
    template_name = 'customer/contactlog-create.html'
    form_class = ContactLogForm
    success_url = reverse_lazy('customers')

    def form_valid(self,form):
        contact_log = form.save(commit=False)
        contact_log.customer_id = self.kwargs['pk']
        contact_log.save()
        return super(ContactLogCreate, self).form_valid(form)

class ContactLogList(LoginRequiredMixin, ListView):
    model = ContactLog
    context_object_name = 'ContactLogs'
    template_name = 'customer/contact_log_list.html'
    def get_context_data(self, **kwargs):
        current_date = date.today()
        context = super().get_context_data(**kwargs)
        context['ContactLogs'] = context['ContactLogs'].filter(next_contact__gt= current_date).order_by('next_contact')
        context["filter"] = ContactLogsFilter(self.request.GET, queryset=self.get_queryset())
        return context