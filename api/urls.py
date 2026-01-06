from django.urls import path
from .views import home, upload_pdf

urlpatterns = [
    path("", home),
    path("upload/", upload_pdf),
]
