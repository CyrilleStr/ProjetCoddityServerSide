from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import TipsSerializer
from .models import Tips

class TipsList(generics.ListCreateAPIView):
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer


class TipsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
