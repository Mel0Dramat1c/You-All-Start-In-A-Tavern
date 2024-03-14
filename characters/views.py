from django.shortcuts import render
from .models import Character


def create_character(request):
    # Logic to handle character creation form submission
    pass


def main_page(request):
    characters = Character.objects.all()
    return render(request, 'main_page.html', {'characters': characters})
    