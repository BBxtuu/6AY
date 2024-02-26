from django.urls import path
from hello import views
from .views import hello

urlpatterns = [
    path('hello/', hello, name="hello"),
    path("<name>", views.hello_there, name="hello_there"),
    path("it_is/me", views.it_is_me, name="it_is_me"),
   
]