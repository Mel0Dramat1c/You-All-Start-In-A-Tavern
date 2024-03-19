from django.http import Http404
from django.shortcuts import render
from .models import Character
from characters.forms import CharacterForm


def main_page(request):
    characters = Character.objects.all()
    return render(request, 'main_page.html', {'characters': characters})


def detail(request, id):
    try:
        character = Character.objects.get(id=id)
    except:
        raise Http404("Character not found")
    return render(request, 'character.html', {"character": character})


def create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.profile = request.user.profile
            character.save()
            # Redirect to character detail page
            return redirect('character_detail', id=character.id)
    else:
        form = CharacterForm()
    return render(request, 'create_a_character.html', {'form': form})
