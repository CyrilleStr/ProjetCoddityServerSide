from django.urls import path, include
from . import views 

urlpatterns = [
    path('add-bin/',views.BinCreate.as_view()),
    path('add-garbage/',views.GargabeCreate.as_view()),
    path('list-bin/',views.BinList.as_view()),
    path('list-garbage/',views.GargabeList.as_view()),
    path('garbages-to-validate/',views.getGarbagesToValidate),
    path('garbages-validation/',views.garbagesValidation)
]