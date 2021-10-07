from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
    
    def test_get(self):
        """GET/ Must return status code 200"""       
        self.assertEqual(self.response.status_code, 200)
        
    def test_template(self):
        self.assertTemplateUsed(self.response, "index.html")