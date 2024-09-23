from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def user_home(request):
    return HttpResponse("Hello, This is a project to test django subdomain")


def user_profile(request, id):
    return JsonResponse({"message":"Hello, This is a project to test django subdomain"})