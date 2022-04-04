from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views 

urlpatterns = [
    path('register/', views.UserCreate.as_view()),
    path('token/', obtain_auth_token),
    path('list/',views.UserList.as_view()),
    path('example/',views.ExampleView.as_view())
]