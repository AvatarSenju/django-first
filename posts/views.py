from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
#from bs4 import BeautifulSoup

from .models import Post

# Create your views here.
def create(request):
    return render(request,"index.html",{"title":"to create"})
def details(request,id):
    instance = get_object_or_404(Post,id=id)
    context ={
    "title":instance.title,
    "instance":instance
    }
    return render(request,"post_details.html",context)
def update(request):
    return HttpResponse("index21.html")
def retrive(request,id=None):
    ins=get_object_or_404(Post,id=id)
    context={"title":ins.updated}
    return render(request,"index.html",context)
def delete(request):
    return HttpResponse("index.htm12l")
def listss(request):
    queryset = Post.objects.all()
    context = {
    "object_list":queryset,
    "title":"List"
    }
    return render(request,"index.html",context)
