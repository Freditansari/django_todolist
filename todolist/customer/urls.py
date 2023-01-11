from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import CustomerList, CustomerCreate, CustomerUpdate, DeleteView,\
    ContactLogCreate

urlpatterns = [
    path('', CustomerList.as_view(), name='customers'),
    path('create/', CustomerCreate.as_view(), name='customer-create'),
    path('contact-log-create/<int:pk>', ContactLogCreate.as_view(), name='contact-log-create'),
    path('update/<int:pk>', CustomerUpdate.as_view(), name='customer-update'),
    path('delete/<int:pk>', DeleteView.as_view(), name='customer-delete'),

]