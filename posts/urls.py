from django.contrib import admin
from django.urls import path,re_path
from . import views as v

app_name="posts"

urlpatterns = [
    path('',v.listss,name='lists'),
    path('create', v.create, name='create'),
    path('update', v.update, name='update'),
    path('retrive/<int:id>/', v.retrive, name='retrive'),
#   re_path(r'^retrive/(?P<id>\d+)/$', v.retrive, name='retrive'),
    path('details/<int:id>/', v.details, name='details'),
    path('delete', v.delete, name='delete'),
]
