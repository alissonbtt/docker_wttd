from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime
from django.shortcuts import resolve_url as r


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Alisson Bittencourt",
            cpf="12345678910",
            email="alison_btt@hotmail.com",
            phone="45-999294016"
        )
        self.obj.save()      
            
    def test_create(self):       
        self.assertTrue(Subscription.objects.exists())
       
    def  test_created_at(self): 
        self.assertIsInstance(self.obj.created_at, datetime)
        
    def test_string(self):
        self.assertEqual('Alisson Bittencourt', str(self.obj))
        
    def test_paid_default_to_false(self):
        self.assertFalse(self.obj.paid)
        
    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
        
        