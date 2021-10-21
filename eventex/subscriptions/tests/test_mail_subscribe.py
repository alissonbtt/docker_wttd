from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class SubscribePostvalid(TestCase):
    def setUp(self):
        data = dict(name='Alisson Bittencourt',
                    cpf='12345678910',
                    email='alison_btt@hotmail.com',
                    phone='45-99929-4016')
         
        self.client.post(r('subscriptions:new'), data) 
        self.email = mail.outbox[0]  
       
    def test_subscription_email_subject(self):      
        expecte = 'Confirmação de inscrição'        
        self.assertEqual(expecte, self.email.subject)
    
    def test_subscrition_email_from(self):        
        expect = 'alisson_servidores@hotmail.com'
        self.assertEqual(expect, self.email.from_email)    
        
    def test_subscrition_email_to(self): 
        expect = ['alisson_servidores@hotmail.com', 'alison_btt@hotmail.com']
        self.assertEqual(expect, self.email.to)
        
        
    def test_subscrition_email_body(self):        
        contents = ['Alisson Bittencourt',
                    '12345678910',
                    'alison_btt@hotmail.com',
                    '45-99929-4016',
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)