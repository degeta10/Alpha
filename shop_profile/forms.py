from django import forms
from django.contrib.auth.models import User
from .models import CreateShop


class ShopForm(forms.ModelForm):

    class Meta:
        model = CreateShop
        fields = ['bname', 'location','opentime','closetime','category','phone']

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email', 'password']
