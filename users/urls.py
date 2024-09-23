from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('profile/', views.user_profile, name='user_profile'),
    # Add more user-specific routes here
]
