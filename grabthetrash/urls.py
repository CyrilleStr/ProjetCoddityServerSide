from django.urls import path, include
from . import views 

urlpatterns = [
    path('add-bin/',views.BinCreate.as_view()),
    path('add-garbage/',views.GargabeCreate.as_view()),
    path('list-bin/',views.BinList.as_view()),
    path('list-garbage/',views.GargabeList.as_view()),
    path('garbages-to-rate/',views.getGarbagesToRate),
    path('garbages-validation/',views.garbagesValidation),
    path('get-coordinates/',views.BinCoordinatesList.as_view()),
    path('delete-all-bin/',views.deleteAllBins),
    path('delete-all-garbages/',views.deleteAllGarbages),
    path('set-all-bins-valid/',views.setAllBinValid),
    path('get-garbages-to-throw/',views.getUserGarbageToThrow),
    path('rate-garbage/',views.postRateGarbage),
    path('throw-garbage/',views.garbageThrown),
    path('get-garbage-thrown/',views.getUserThrownGarbage),
]