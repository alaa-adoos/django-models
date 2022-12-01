from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class Snakstest(TestCase):
    def test_home_page_status(self):
        url=reverse('home')
        respones=self.client.get(url)
        self.assertEqual(respones.status_code,200)
    
    def test_snack_page_status(self):
        url=reverse('snacks')
        respones=self.client.get(url)
        self.assertEqual(respones.status_code,200)
    def test_home_page_template(self):
        url=reverse('home')
        respones=self.client.get(url)
        self.assertTemplateUsed(respones,'home.html')
    def test_snack_page_template(self):
        url=reverse('snacks')
        respones=self.client.get(url)
        self.assertTemplateUsed(respones,'snack_list.html')