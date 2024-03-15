from django.contrib import admin
from characters.models import Character, CharacterClass, CharacterRace
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(CharacterRace)
