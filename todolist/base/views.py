from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from django.db import models as db_models
from django.forms import ModelForm

from django.contrib.auth.models import User

from .models import Task

class RegisterForm(ModelForm):
    username = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "password"]
class CustomLoginView( LoginView):
   template_name = 'base/login.html'
   fields ='__all__'
   redirect_authenticated_user = True
   def get_success_url(self):
       return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    # form_class = RegisterForm
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            if user is not None:
                login(self.request, user)
            return super(RegisterPage, self).form_valid(form)
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('tasks')
    #     return super(RegisterPage, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name = 'Tasks'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['Tasks']=context['Tasks'].filter(user=self.request.user)
        context['count']=context['Tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['Tasks'] = context['Tasks'].filter(title__icontains=search_input)

        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model=Task
    context_object_name = 'task'
    # how to change the name of template name so we don't have to use task_detail.html
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model= Task
    # fields='__all__'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields='__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')