from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from characters.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'character_class', 'character_race', 'level',
            'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom',
            'charisma', 'items', 'features', 'bio']


def __init__(self, *args, **kwargs):
    super(CharacterForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.layout = Layout(
        'name', 'character_class', 'character_race', 'level', 'strength',
        'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
        'items', 'features', 'bio',
        Submit('submit', 'Submit', css_class='btn btn-primary')
        )
