from django import forms
from characters.models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'character_class', 'character_race', 'level', 'strength', 'dexterity', 'constitution',
                  'intelligence', 'wisdom', 'charisma', 'items', 'features', 'bio']


    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation rules if needed
        return cleaned_data