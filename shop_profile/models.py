from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CreateShop(models.Model):
    user = models.ForeignKey(User, default=1)
    bname = models.CharField(max_length=25)
    location = models.CharField(max_length=500)
    geolocation = models.CharField(max_length=200)
    opentime = models.TimeField(blank=True,null=True)
    closetime = models.TimeField(blank=True,null=True)
    category = models.CharField(max_length=200)
    owner = models.CharField(max_length=20)
    phone= models.CharField(max_length=10)
    logo = models.FileField()
    btag = models.CharField(max_length=20)
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.bname

