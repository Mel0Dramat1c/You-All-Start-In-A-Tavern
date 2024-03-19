from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name="home"),
    path("create", views.create, name="character_create"),
    path("<int:id>", views.detail, name="character_detail"),
]
