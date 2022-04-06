from django.urls import path, include
from . import views 

urlpatterns = [
    path('',views.BinCreate.as_view()),
]