from django import forms
from django.forms.widgets import NumberInput

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

    cpf = forms.IntegerField(label="CPF/GPF 14-digit Number")
    Date_of_Birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    Month = forms.ChoiceField(choices=MONTH_CHOICES)
    Year = forms.ChoiceField(choices=YEAR_CHOICES)










