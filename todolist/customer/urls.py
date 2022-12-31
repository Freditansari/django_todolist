from django.urls import path
from django.contrib.auth.views import LogoutView


from .views import CustomerList

urlpatterns = [
    path('', CustomerList.as_view(), name='customers'),

]