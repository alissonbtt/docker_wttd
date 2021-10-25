from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números', 'length')
    
class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=150)
    cpf = forms.CharField(max_length=11, validators=[validate_cpf])
    email = forms.EmailField()
    phone = forms.CharField()
    
    def clean_name(self):
        name = self.cleaned_data['name'].title()
        return name
        