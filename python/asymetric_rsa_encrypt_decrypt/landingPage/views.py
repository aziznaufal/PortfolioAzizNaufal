from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'LandingPage/post_list.html', {'posts': posts})

def home(request):
    posts = Post.objects.all()
    print('masuk ke landingPage')
    return render(request, 'LandingPage/home.html')