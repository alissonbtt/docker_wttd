from django import forms


class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=150)
    cpf = forms.CharField(max_length=11)
    email = forms.EmailField()
    phone = forms.CharField()