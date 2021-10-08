from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail

        
class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
    
    def test_get(self):
        """Get /inscricao/ retorna status code 200"""
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):        
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
        
    def test_html(self):
        tags = (('<form',1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
      
    def test_csrf(self):
        """Verifica se a página possui as csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        
    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
        
    

class SubscribePostvalid(TestCase):
    def setUp(self):
         data = dict(name='Alisson Bittencourt',
                    cpf='12345678910',
                    email='alison_btt@hotmail.com',
                    phone='45-99929-4016')
         self.resp = self.client.post('/inscricao/', data)
    
    def test_post(self):
        """Valid POST should redirect to /inscricao/"""                
        self.assertEqual(302, self.resp.status_code)
        
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
        
   

                
                
class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})
        
    def test_post(self):
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
        
    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
        
    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)
        
        
class SubscribeSuccesMessage(TestCase):
    def test_message(self):
        data =  dict(name='Alisson Bittencourt',
                    cpf='12345678910',
                    email='alison_btt@hotmail.com',
                    phone='45-99929-4016')
        
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')
        