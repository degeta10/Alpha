from django.shortcuts import render
from django.template import loader
from .models import CreateProfile

# Create your views here.
def index(request):
    #all_shops=CreateProfile.objects.all()

    template=loader.get_template('shop_profile/index.html')

    #context={'all_shops':all_shops}

    return render(request,'shop_profile/index.html',context=None)











    9