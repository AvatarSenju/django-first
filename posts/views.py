from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
#from bs4 import BeautifulSoup

from .models import Post

# Create your views here.
def create(request):
    return render(request,"index.html",{"title":"to create"})
def details(request):
    querys=Post.objects.all()

    if request.user.is_authenticated:
        context={
        "title":"good",
        "ls":querys
        }

    else:
        context={"title":"bad"}
    return render(request,"index.html",context)
def update(request):
    return HttpResponse("index21.html")
def retrive(request,id=None):
    ins=get_object_or_404(Post,id=id)
    context={"title":ins.updated}
    return render(request,"index.html",context)
def delete(request):
    return HttpResponse("index.htm12l")
