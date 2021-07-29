from Guest import forms
from .models import Review
from django.forms import ModelForm

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=["review"]

