from django.contrib import admin
from django.urls import path,re_path
from . import views as v

app_name="posts"

urlpatterns = [
    path('',v.listss,name='lists'),
    path('create', v.create, name='create'),
    path('edit/<int:id>/', v.update, name='update'),
    path('retrive/<int:id>/', v.retrive, name='retrive'),
#   re_path(r'^retrive/(?P<id>\d+)/$', v.retrive, name='retrive'),
    path('details/<int:id>/', v.details, name='details'),
    path('delete/<int:id>/', v.delete, name='delete'),
]
