from django.urls import path
from app1.views import *
app_name='somgthing1'

urlpatterns=[ 
    path('jinja/',jinja,name='jinja'),

]