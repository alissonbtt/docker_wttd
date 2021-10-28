from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    fixtures = ['keynotes.json']
    
    def setUp(self):
        self.response = self.client.get(r('home'))
    
    def test_get(self):
        """GET/ Must return status code 200"""       
        self.assertEqual(self.response.status_code, 200)
        
    def test_template(self):
        self.assertTemplateUsed(self.response, "index.html")
        
    def test_subscrition_links(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)
        
    def test_speakers(self):
        contents = [
			'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
			'Grace Hopper',
			'http://hbn.link/hopper-pic',
			'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
			'Alan Turing',
			'http://hbn.link/turing-pic',
		]
        
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
       
    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)