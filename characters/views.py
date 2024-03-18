from django.http import Http404
from django.shortcuts import render
from .models import Character


def create_character(request):
    pass


def main_page(request):
    characters = Character.objects.all()
    return render(request, 'main_page.html', {'characters': characters})


def detail(request, id):
    try:
        character = Character.objects.get(id=id)
    except:
        raise Http404("Character not found")
    return render(request, 'character.html', {"character": character})
