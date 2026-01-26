from django.urls import path
from .views import home, upload_pdf, search_view

urlpatterns = [
    path("", home, name="home"),
    path("upload/", upload_pdf, name="upload"),
    path("search/", search_view, name="search"),
]
