from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from profiles.models import Profile


# Create your models here.
class CharacterClass(models.Model):
    """
    Models for the character classes.
    """
    name = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.name


class CharacterRace(models.Model):
    """
    Models for the character races.
    """
    name = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.name


class Character(models.Model):
    """
    Model for user's characters (linked to a user's profile).
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    character_class = models.ForeignKey(
        CharacterClass, on_delete=models.CASCADE, null=False, blank=False)
    character_race = models.ForeignKey(
        CharacterRace, on_delete=models.CASCADE, null=True, blank=True)
    level = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        null=False, blank=False
    )
    strength = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        null=False, blank=False
    )
    dexterity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        null=False, blank=False
    )
    constitution = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        null=False, blank=False
    )
    intelligence = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        null=False, blank=False
    )
    wisdom = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        null=False, blank=False
    )
    charisma = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        null=False, blank=False
    )
    items = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
