from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from grabthetrash.serializers import *
from .models import *

def upload_to(instance,filename):
    return 'bin/{filename}'.format(filename=filename)

class BinCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, format=None):
        print(request.data)
        serializer = BinSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BinList(generics.ListAPIView):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer

class GarbageCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, format=None):
        print(request.data)
        serializer = GarbageSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GarbageList(generics.ListAPIView):
    queryset = Garbage.objects.all()
    serializer_class = GarbageSerializer