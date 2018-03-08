from django.contrib import admin
from django.urls import path,re_path
from . import views as v

urlpatterns = [

    path('create', v.create, name='create'),
    path('update', v.update, name='update'),
    re_path(r'^retrive/(?P<id>\d+)/$', v.retrive, name='retrive'),
    path('details', v.details, name='details'),
    path('delete', v.delete, name='delete'),
]
