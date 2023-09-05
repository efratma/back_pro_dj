from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.register),
    path('problem/<str:problem_name>/', views.problem_solver),
    path('user-exercises/', views.ListUserExercises.as_view(), name='list-user-exercises'),
]

