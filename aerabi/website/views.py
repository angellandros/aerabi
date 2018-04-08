from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def blog(request):
    from .models import BlogPost
    posts = BlogPost.objects.all()
    return render(request, 'website/blog.html', context={'posts': posts})


def post(request, url):
    from .models import BlogPost
    the_post = BlogPost.objects.get(url=url)
    return render(request, 'website/blog_post.html', context={'post': the_post})
