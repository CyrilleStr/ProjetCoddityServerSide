from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from grabthetrash import serializers
from .models import *

class BinCreate(generics.CreateAPIView):
    queryset = Bin.objects.all()
    serializers_class = serializers.BinSerializer

