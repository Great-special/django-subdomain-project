from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<int:id>/', views.blog_post, name='blog_post'),
    # Add more blog-specific routes here
]
