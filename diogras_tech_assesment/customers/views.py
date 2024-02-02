from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from customers.models import Customer
from customers.forms import CustomerForm

# Create your views here.

class CustomersView(ListView):
    template_name='customers.html'
    model = Customer
    context_object_name = 'customers'

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.all()

class AddCustomerView(FormView):
    form_class = CustomerForm
    template_name = 'add_new_customer.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if not form.is_valid():
            return super().form_invalid(form)
        form.save()
        return super().form_valid(form)

@require_http_methods(['DELETE'])
def delete_customer(request, id):
    Customer.objects.get(pk=id).delete()

    customers = Customer.objects.all()

    return render(request, 'customer_list.html', {'customers' : customers})
