from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def user_home(request):
    return HttpResponse("Hello, This is a user")


def user_profile(request, id):
    return JsonResponse({"message":"Hello, This is a user profile"})