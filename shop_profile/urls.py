from django.conf.urls import url
from . import views

app_name = 'shop_profile'

urlpatterns = [
     url(r'^$',views.index,name='index'),
    url(r'^register/$',views.index,name='index'),
]