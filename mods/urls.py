from django.urls import path
from .views import ModListView



urlpatterns = [
  path("", ModListView.as_view(), name="mod_list"),
]             