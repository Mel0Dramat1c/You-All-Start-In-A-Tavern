from django.http import Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Character
from characters.forms import CharacterForm


def main_page(request):
    characters = Character.objects.all()
    return render(request, 'the_tavern/main_page.html',
                  {'characters': characters})


def detail(request, id):
    try:
        character = Character.objects.get(id=id)
    except:
        raise Http404("Character not found")
    return render(request, 'character.html', {"character": character})


def create(request):
    form = CharacterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            character = form.save(commit=False)
            character.profile = request.user.profile
            character.save()
            messages.success(request, "Your character has been created!")
            # Redirect to character page
            return redirect(reverse('character_detail', kwargs={'id': character.id}))
        messages.error(request, "Error! Please try again.")
    return render(request, 'create_a_character.html', {'form': form})


def edit(request, id):
    character = get_object_or_404(Character, id=id)
    if not character.profile.user == request.user:
        messages.error(request, "Error. Invalid credentials.")
        return redirect('home')
    
    form = CharacterForm(request.POST or None, instance=character)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Your character has been updated!")
            # Redirect to character page
            return redirect(reverse('character_detail', kwargs={'id': id}))
        messages.error(request, "Error! Please try again.")
    return render(request, 'edit_a_character.html',
                  {'form': form, 'character': character})


def delete(request, id):
    character = get_object_or_404(Character, id=id)
    if not character.profile.user == request.user:
        messages.error(request, "Error. Invalid credentials.")
        return redirect('home')
    character.delete()
    messages.success(request, "Your character has been deleted!")
    return redirect('home')
