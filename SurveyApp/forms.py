from django import forms

# Create your forms here.

CITY_CHOICES =(
    ("1", "New York"),
    ("2", "Washington"),
    ("3", "Los Angeles"),
    ("4", "Houston"),
    ("5", "Las Vegas"),
)

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=150)
    city = forms.ChoiceField(choices=CITY_CHOICES)
    pincode = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.IntegerField()