from django.test import TestCase
from subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
    
    def test_get(self):
        """Get /inscricao/ retorna status code 200"""
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        respose = self.client.get('/inscricao/')
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
        
    def test_html(self):
        """Verifica se o html possui as tags de input"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"', 1)
        self.assertContains(self.resp, 'type="submit"', 1)
      
    def test_csrf(self):
        """Verifica se a página possui as csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        
    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
        
    def test_form_has_fields(self):
        form = self.resp.context['form']
        self.assertEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))