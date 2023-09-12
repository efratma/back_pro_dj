from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.register),
    path('problem/<str:problem_name>/', views.problem_solver),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('request-password-reset/', views.request_password_reset, name='request-password-reset'),
    path('reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset-password'),



]

