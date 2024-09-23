from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index_views(request):
    return HttpResponse("Hello, This is a project to test django subdomain")


def home_views(request):
    return JsonResponse({"message":"Hello, This is a project to test django subdomain"})