from django import forms
from django.contrib.auth.models import User

from .models import CreateProfile


class ShopForm(forms.ModelForm):

    class Meta:
        model = CreateProfile
        fields = ['bname', 'location', 'geolocation', 'opentime','closetime','category','owner','phone','logo','btag','website']
