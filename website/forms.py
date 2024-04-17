# forms.py
from django import forms

class BMICalculationForm(forms.Form):
    height = forms.FloatField(label='Taille / cm')
    weight = forms.FloatField(label='Poids / kg')
    age = forms.IntegerField(label='Âge')
    gender = forms.ChoiceField(choices=[('male', 'Masculin'), ('female', 'Féminin')], label='Sexe')
    activity_level = forms.ChoiceField(choices=[
        ('little', 'Peu ou pas d\'exercice / travail de bureau'),
        ('light', 'Exercice léger / sports 1 à 3 jours/semaine'),
        ('moderate', 'Exercice modéré, sports 3 à 5 jours/semaine'),
        ('heavy', 'Exercice intense / sports 6 à 7 jours/semaine'),
        ('very_heavy', 'Exercice très intense / travail physique / entraînement 2 fois/jour')
    ], label='Niveau d\'activité')