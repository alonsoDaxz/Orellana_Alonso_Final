from django import forms
from .models import Inscrito

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'
