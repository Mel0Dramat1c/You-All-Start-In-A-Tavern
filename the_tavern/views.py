from django.shortcuts import render
from django.http import HttpResponse
from characters.models import Character
from characters.forms import CharacterForm


def main_page(request):
    characters = Character.objects.all()
    return render(request, 'the_tavern/main_page.html', {'characters': characters})