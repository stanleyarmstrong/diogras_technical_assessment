from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from customers.models import Customer

# Create your tests here

class TestCustomerURLS(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer1 = Customer(
            first_name='John', last_name='Doe',
            address='123 Main St', city='Exampleville', zipcode='12345', state='CA'
        )
        self.customer1.save()
        Customer.objects.create(
            first_name='Jane', last_name='Smith',
            address='456 Oak St', city='Sampletown', zipcode='54321', state='NY'
        )
        Customer.objects.create(
            first_name='Bob', last_name='Johnson',
            address='789 Elm St', city='Testburg', zipcode='98765', state='TX'
        )



    
    @classmethod
    def setUpTestData(cls):
        # Create instances of the Customer model for testing
        cls.customer1 = Customer(
            first_name='John', last_name='Doe',
            address='123 Main St', city='Exampleville', zipcode='12345', state='CA'
        )
        cls.customer2 = Customer(
            first_name='Jane', last_name='Smith',
            address='456 Oak St', city='Sampletown', zipcode='54321', state='NY'
        )
        cls.customer3 = Customer(
            first_name='Bob', last_name='Johnson',
            address='789 Elm St', city='Testburg', zipcode='98765', state='TX'
        )


    def test_get_all(self):
        url = reverse('index')

        response = self.client.get(url)

        self.assertEqual(len(response.context['customers']), Customer.objects.count())

    def test_add(self):
        url = reverse('add-customer')
        form_data = {
            'first_name': 'Joe',
            'last_name': 'Doe',
            'address': '123 Main St',
            'city': 'Exampleville',
            'zipcode': '12345',
            'state': 'CA',
        }


        response = self.client.post(url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Customer.objects.count) 

    def test_add_false_state(self):
        url = reverse('add-customer')
        form_data = {
            'first_name': 'Joe',
            'last_name': 'Doe',
            'address': '123 Main St',
            'city': 'Exampleville',
            'zipcode': '12345',
            'state': 'YYZ',
        }


        response = self.client.post(url, form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Customer.objects.filter(first_name='Joe', last_name='Doe').exists()) 

    def test_add_false_zip(self):
        url = reverse('add-customer')
        form_data = {
            'first_name': 'Joe',
            'last_name': 'Doe',
            'address': '123 Main St',
            'city': 'Exampleville',
            'zipcode': '123456',
            'state': 'CA',
        }


        response = self.client.post(url, form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Customer.objects.filter(first_name='Joe', last_name='Doe').exists()) 

    def test_delete(self):
        url = reverse('delete_customer', args=[self.customer1.id])


        response = self.client.delete(url)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Customer.objects.filter(first_name='John', last_name='Doe').exists()) 