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
    
    # Pass the URLs to the template context
    context_url = {
    
        'blog_post_url': blog_post_url,  # With post ID included
    }
    return render(request, 'index.html', context=context_url)