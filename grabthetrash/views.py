from gc import garbage
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from grabthetrash.serializers import *
from .models import *

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

class BinCoordinatesList(generics.ListAPIView):
    queryset = Bin.objects.filter(isAccepted=True)
    serializer_class = BinCoordinatesSerializer

class GargabeCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, format=None):
        print(request.data)
        serializer = GarbageSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GargabeList(generics.ListAPIView):
    queryset = Garbage.objects.all()
    serializer_class = GarbageSerializer


@api_view(['GET'])
def getGarbagesToValidate(request):
    garbages = Garbage.objects.all().filter(isRatingDone=False)[:3]
    garbageSerializer = GarbageSerializer(garbages,many=True)
    if garbages.__len__ == 0:
        return Response(garbageSerializer.errors, status=status.HTTP_410_GONE)
    else:
        return Response(garbageSerializer.data)

@api_view(['POST'])
def garbagesValidation(request):
    user = User.objects.get(id=request.user.id)
    if request.POST['pk1'] and request.POST['pk2'] and request.POST['pk3'] and request.POST['answer1'] and request.POST['answer2'] and request.POST['answer3']:
        if request.POST['pk1'] != "0" :
            garbage1:Garbage = get_object_or_404(Garbage,pk=request.POST['pk1'])
            garbage1.addVerdict(user,request.POST['answer1'])
            garbage1.save()
        if request.POST['pk2'] != "0" :
            garbage2:Garbage = get_object_or_404(Garbage,pk=request.POST['pk2'])
            garbage2.addVerdict(user,request.POST['answer2'])
            garbage2.save()
        if request.POST['pk3'] != "0" :
            garbage3:Garbage = get_object_or_404(Garbage,pk=request.POST['pk3'])
            garbage3.addVerdict(user,request.POST['answer3'])
            garbage3.save()
        
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def setAllBinValid(request):
    bins = Bin.objects.all()
    for bin in bins:
        bin.isAccepted = True
        bin.isVerified = True
        bin.save()
    return Response(status=status.HTTP_200_OK)

