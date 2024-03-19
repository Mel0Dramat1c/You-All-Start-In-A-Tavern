from django.urls import path
from . import views


urlpatterns = [
    path("", views.main_page, name="home"),
    path("create/", views.create, name="character_create"),
    path("edit/<int:id>/", views.edit, name="character_edit"),
    path("<int:id>/", views.detail, name="character_detail"),
    path("delete/<int:id>/", views.delete, name="character_delete"),
]
