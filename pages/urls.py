from django.urls import path
from .views import about, home, contact
from . import views

urlpatterns = [
  path("", home, name="home"),
  path("contact/", views.contact, name="contact"),
]