from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def blog_home(request):
    return HttpResponse("Hello, This is a blog")


def blog_post(request, id):
    return JsonResponse({"message":"Hello, This is a blog post"})