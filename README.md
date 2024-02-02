# Customers APP

## Design Decisions
For the frontend, I used a combination of Django templates and HTMX to render my application. HTMX allowed me to access the statefulness in the application without having to set up any JavaScript library in order to achieve this.

Instead, the application's endpoints served HTML responses that HTMX then updated the states. This was in place of using Django REST to send JSON to the frontend of the application. For adding Customers to the database, I used the Django Forms API which on a successful run would update the customer table. On deletion, I sent a delete request with the item's id which deleted the item from the list and updated the outer HTML of the customers list through HTMX swapping.

The application has three URL views: index, add-customer, delete_customer which shows the list of customers, adds a customer to active customers, and deletes a customer respectively. In order to verify these , I used unittesting around the url endpoints adding correct and incorrect data in the form for add-customer and verified the others by getting and deleting data. 

## How to Run
1. Create a new Python virtual environment 
`virutalenv diogras`
2. Activate Python virtual environment: `source diogras/bin/activate`
3. Install all requirements: `pip install -r requirements.txt`
4. From the diogras_tech_assessment directory run: `python manage.py runserver` 
5. The app should be running at  **http://localhost:8000**

## How to Run Tests
Assuming the steps in How To Run were done the tests can be run via 
`python manage.py test`