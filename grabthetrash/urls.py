from django.urls import path, include
from . import views 

urlpatterns = [
    path('add-bin/',views.BinCreate.as_view()),
    path('list-bin/',views.BinList.as_view()),
    path('add-gargage/',views.GarbageCreate.as_view()),
    path('list-bin/',views.GarbageList.as_view()),
]