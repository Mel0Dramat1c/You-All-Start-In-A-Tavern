from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Lists fields on display in admin.
    """


    list_display = ("user", "image_preview")
