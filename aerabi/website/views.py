from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def blog(request):
    from .models import BlogPost
    posts = BlogPost.objects.all()
    return render(request, 'website/blog.html', context={'posts': posts})
