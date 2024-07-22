from django.test import TestCase
from django.urls import reverse, resolve
from specialties import views 
""" TESTCASE DERIVA DE UNITTEST DO PYTHON """
 
class TestUrlView(TestCase):

    def test_home_url_equals_view(self):
        url = reverse('specialties:home')
        self.assertEqual(url, '/')

    def test_about_url_equals_view(self):
        url = reverse('specialties:about')
        self.assertEqual(url, '/about/')

class RecipeViewsTest(TestCase):

    def test_recipe_home_views_function(self):
        view = resolve(reverse('specialties:home'))
        self.assertEqual(view.func, views.home)
        
    
    def test_recipe_about_views_function(self):
        view = resolve(reverse('specialties:about'))
        self.assertEqual(view.func, views.about) 