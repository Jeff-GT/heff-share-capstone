from django.urls import path
from .views import ModListView, ModUploadView, ModDetailView, upload_mod_images



urlpatterns = [
  path("", ModListView.as_view(), name="mods_list"),
  path("upload/", ModUploadView.as_view(), name="mod_upload"),
  path("<str:game>/<int:pk>/", ModDetailView.as_view(), name="mod_detail"),
  path("<str:game>/<int:pk>/img-upload/", upload_mod_images, name="image_upload")

]          