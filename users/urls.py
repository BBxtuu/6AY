from django.urls import path
from .views import profile_view
from . import views

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('contact/', views.contact, name='contact'),
]