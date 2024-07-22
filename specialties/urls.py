from django.urls import path
from . import views

#recipes:recipe
app_name = 'specialties'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]