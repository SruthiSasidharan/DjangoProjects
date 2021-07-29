from django import forms
from .models import MyUser,Library
from .admin import UserCreationForm
from django.forms import ModelForm
class RegForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["email","phonenumber","First_name","Last_name","address","password1","password2"]

class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)


class LibraryForm(forms.ModelForm):
    class Meta:
        model=Library
        fields="__all__"
