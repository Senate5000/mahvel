from django import forms
from combodb.models import Game, Character, Ability, Combo


class GameForm(forms.ModelForm):
    class Meta:
        model = Game


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character


class AbilityForm(forms.ModelForm):
    class Meta:
        model = Ability


class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
