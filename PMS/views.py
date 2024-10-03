from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django_hosts.resolvers import reverse


def index_views(request):
    return HttpResponse("Hello, This is a project to test django subdomain")


def home_views(request):
    return JsonResponse({"message":"Hello, This is a project to test django subdomain"})



def homepage(request):
    post_id = 1
    blog_post_url = reverse('blog_post', kwargs={'id': post_id}, host='blog')
    blog_home_url = reverse('blog_home', host='blog')
    user_home_url = reverse('user_home', host='user')
    print(blog_home_url)
    # Pass the URLs to the template context
    context_url = {
        'blog_home_url':blog_home_url,
        'blog_post_url': blog_post_url,  # With post ID included
        'user_home_url':user_home_url
    }
    return render(request, 'index.html', context=context_url)