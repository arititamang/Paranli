from django import forms
from django.forms.widgets import NumberInput
from captcha.fields import CaptchaField
from .models import Contact



MONTH_CHOICES = (
    ("01", "January"),
    ("02", "February"),
    ("03", "March"),
    ("04", "April"),
    ("05", "May"),
    ("06", "June"),
    ("07", "July"),
    ("08", "August"),
    ("09", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),

)
YEAR_CHOICES = [
    ('1990', '1899'),
    ('1997', '1898'),
    ('1896', '1994'),
    ('1895', '1894'),
    ('1991', '1893'),
    ('1892', '1990'),
    ('1891', '1890'),
    ('1890', '1898'),
    ('1991', '1992'),
    ('1895', '1994'),
    ('1991', '1893'),
    ('1892', '1990'),
]

class StudentForm(forms.Form):

    cpf = forms.IntegerField(label="CPF/GPF ",
                             help_text="Enter 14 digit  number"
                             )
    Date_of_Birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    Month = forms.ChoiceField(choices=MONTH_CHOICES)
    Year = forms.ChoiceField(choices=YEAR_CHOICES)

class Form(forms.Form):
    captcha = CaptchaField()




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['cpf', 'dob', 'month', 'otp','year']


        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your Name'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required':'required'}),
            'otp':  forms.TextInput(attrs={'class': 'otp',  'placeholder' : 'Your message...'}),
        }






