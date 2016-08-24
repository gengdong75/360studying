from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from home.views import home_page


# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
   
    def test_home_page2(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
   
