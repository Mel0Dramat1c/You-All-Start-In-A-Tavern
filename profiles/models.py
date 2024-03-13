from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Model for user's profile (extending from the default User model).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField("image", default="placeholder")

    def image_preview(self):
        from django.utils.html import format_html
        return format_html(f"<img src='{self.image.url}' height='150'>")

    def __str__(self):
        return self.user.username
