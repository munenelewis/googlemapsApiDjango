from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
]