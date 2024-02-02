from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from customers.models import Customer

# Create your views here.

class CustomersView(ListView):
    template_name='customers.html'
    model = Customer
    context_object_name = 'customers'

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.all()


@require_http_methods(['DELETE'])
def delete_customer(request, id):
    Customer.objects.get(pk=id).delete()

    customers = Customer.objects.all()

    return render(request, 'customers.html', {'customers' : customers})
