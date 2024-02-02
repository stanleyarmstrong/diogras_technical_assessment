from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.TextField()
    city = models.TextField()
    zipcode = models.TextField()
    state = models.TextField()