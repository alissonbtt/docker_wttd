from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime

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