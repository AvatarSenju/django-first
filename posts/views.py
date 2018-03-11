from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
#from bs4 import BeautifulSoup

from .models import Post
from .forms import PostForm
# Create your views here.
def create(request):
    form =PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request,"Success")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request,"NOT DONE")
    context = {
    "form":form,
    }
    return render(request,"post_form.html",context)
def details(request,id):
    instance = get_object_or_404(Post,id=id)
    context ={
    "title":instance.title,
    "instance":instance
    }
    return render(request,"post_details.html",context)
def update(request,id=None ):
    instance = get_object_or_404(Post,id=id)
    form =PostForm(request.POST or None ,instance=instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request,"Success")
        return HttpResponseRedirect(instance.get_absolute_url())

    # else:
    #     messages.error(request,"NOT DONE")
    context ={
    "title":instance.title,
    "instance":instance,
    "form":form,
    }

    return render(request,"post_form.html",context)
def retrive(request,id=None):
    ins=get_object_or_404(Post,id=id)
    context={"title":ins.updated}
    return render(request,"base.html",context)
def delete(request,id=None):
    instance = get_object_or_404(Post,id=id)
    messages.success(request,"Deleted")
    instance.delete()
    return redirect("posts:lists")
def listss(request):
    queryset = Post.objects.all()
    context = {
    "object_list":queryset,
    "title":"List"
    }
    return render(request,"post_list.html",context)
