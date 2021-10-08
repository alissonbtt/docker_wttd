from subscriptions.forms import SubscriptionForm
from django.test import TestCase


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()    

    def test_form_has_fields(self):
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))
        