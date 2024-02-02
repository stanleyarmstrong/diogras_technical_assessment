from django.forms import ModelForm, CharField, ChoiceField, Select, ValidationError, TextInput
from django.utils.translation import gettext_lazy as _
from customers.models import Customer

class CustomerForm(ModelForm):
    STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
    )
    first_name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    address = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    city = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    state = ChoiceField(choices=STATE_CHOICES, widget=Select(attrs={'class': 'form-select'}))
    zipcode = CharField(max_length=5, widget=TextInput(attrs={'class': 'form-control'}))



    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "address", "city", "zipcode", "state"]
        labels = {
            "first_name": _("First Name:"),
            "last_name": _("Last Name:"),
            "address": _("Address:"),
            "city": _("City:"),
            "zipcode": _("ZIP Code:"),
            "state": _("State:"),
        }
    def clean_state(self):
        # Custom validation for the 'state' field
        state = self.cleaned_data.get('state')
        valid_states = [choice[0] for choice in self.STATE_CHOICES]

        if state not in valid_states:
            raise ValidationError('Invalid state selected.')
        

        return state

    def clean_zip(self):
        zipcode = self.cleaned_data.get('zipcode')
        if not zipcode.isdigit() or len(zipcode) != 5:
            raise ValidationError('Invalid ZIP Code: ZIP Code must be a 5 digit number')

        return zipcode

    