from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts=Post.objects.all()
    n=len(posts)
    return render(request,'index.html',{'posts': posts})


def post(request,pk):
    posts=Post.objects.get(id=pk)  ##Post is the model name, it is going to get the particular post, which has id of pk
    return render(request,'posts.html',{'posts': posts})