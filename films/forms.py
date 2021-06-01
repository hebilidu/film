from django import forms
from .models import Director, Film


class DirectorModelForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class FilmModelForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
