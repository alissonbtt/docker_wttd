from subscriptions.forms import SubscriptionForm
from django.test import TestCase


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_cpf_is_digit(self):
        form = self.make_validated_form(cpf='12345678abc')  
        self.assertFormErrorCode(form, 'cpf', 'digits' )
        
    def test_cpf_has_11_digits(self):       
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length' )
        
    def test_name_must_capitalize(self): 
        """Name must be capitalize"""
        form = self.make_validated_form(name='ALISSON bittencourt')
        self.assertEqual('Alisson Bittencourt', form.cleaned_data['name'] )
        
    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)
        
    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)
        
    def test_must_inform_email_or_phone(self):
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))
        
    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)
        
        
    def make_validated_form(self, **kwargs):
        valid = dict(
            name="Alisson Bittencourt",
            cpf="12345678910",
            email="alison_btt@hotmail.com",
            phone="45-999294016"
        )
        
        data = dict(valid, **kwargs)
        
        form = SubscriptionForm(data=data)
        form.is_valid()
        
        return form