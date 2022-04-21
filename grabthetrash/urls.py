from django.urls import path, include
from . import views 

urlpatterns = [
    path('add-item/',views.ItemCreate.as_view()),
    path('list-item/',views.ItemList.as_view()),
    path('items-to-validate/',views.getItemsToValidate),
    path('items-validation/',views.itemsValidation)
]