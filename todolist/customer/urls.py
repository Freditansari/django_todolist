from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import CustomerList, CustomerCreate, CustomerUpdate, DeleteView

urlpatterns = [
    path('', CustomerList.as_view(), name='customers'),
    path('create/', CustomerCreate.as_view(), name='customer-create'),
    path('update/<int:pk>', CustomerUpdate.as_view(), name='customer-update'),
    path('delete/<int:pk>', DeleteView.as_view(), name='customer-delete'),

]