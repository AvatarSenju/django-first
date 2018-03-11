from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        #meta must be capital
        model =Post
        fields ={
        "content",
        "title",
        }
