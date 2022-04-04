from django.urls import path, include
from rest_framework import routers
from . import views 

urlpatterns = [
    path('tips/', views.TipsList.as_view()),
    path('tips/<int:pk>/', views.TipsDetail.as_view()),
]