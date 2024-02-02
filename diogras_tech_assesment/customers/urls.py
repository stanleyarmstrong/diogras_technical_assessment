from django.urls import path
from customers import views

urlpatterns = [
    path('', views.CustomersView.as_view(), name='index'),
    path('customers/add', views.AddCustomerView.as_view(), name='add-customer'),
    path('customers/<int:id>/delete', views.delete_customer, name='delete_customer')
]