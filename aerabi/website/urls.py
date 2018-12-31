from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('works/', views.works, name='works'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:url>/', views.post, name='post'),
    path('cv/', views.cv, name='cv'),
]
