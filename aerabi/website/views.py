from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def about(request):
    from .models import Page
    page = Page.objects.get(url='about')
    return render(request, 'website/about.html', context={'page': page})


def blog(request):
    from .models import BlogPost
    posts = BlogPost.objects.all()
    return render(request, 'website/blog.html', context={'posts': posts})


def cv(request):
    from .models import Page
    page = Page.objects.get(url='cv')
    return render(request, 'website/cv.html', context={'page': page})


def post(request, url):
    from .models import BlogPost
    the_post = BlogPost.objects.get(url=url)
    return render(request, 'website/blog_post.html', context={'post': the_post})
