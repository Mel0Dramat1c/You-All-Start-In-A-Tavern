from django.contrib import admin
from characters.models import Character, CharacterClass, CharacterRace
# Register your models here.

admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(CharacterRace)
