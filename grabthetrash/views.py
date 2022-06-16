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
    def post(self, request, format=None):
        print(request.data)
        serializer = BinSerializer(data=request.data)
        if serializer.is_valid():
             bin = serializer.save()
             data:dict = {
                 "id": str(bin.id),
                 "latitude": str(bin.latitude),
                 "longitude": str(bin.longitude),
                 "discard": "False",
                 "accepted" : "False",
             }
             return Response(data, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BinList(generics.ListAPIView):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer

class BinCoordinatesList(generics.ListAPIView):
    queryset = Bin.objects.filter(isAccepted=True)
    serializer_class = BinCoordinatesSerializer

class GargabeCreate(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = GarbageSerializer(data=request.data)
        if serializer.is_valid():
             garbage = serializer.save()
             data:dict = {
                 "id": str(garbage.id),
                 "latitude": str(garbage.latitude),
                 "longitude": str(garbage.longitude),
                 "discard": "False",
                 "accepted" : "False",
             }
             return Response(data, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GargabeList(generics.ListAPIView):
    queryset = Garbage.objects.all()
    serializer_class = GarbageSerializer



@api_view(['GET'])
def getUserGarbageToThrow(request):
        garbages = Garbage.objects.all().filter(owner=request.user,discard=False)[:20]
        if garbages.__len__ != 0:
            data = []
            for garbage in garbages:
                data.append(garbage.format())
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_410_GONE)

@api_view(['GET'])
def getGarbagesToRate(request):
    garbages = Garbage.objects.all().filter(isRatingDone=False).exclude(owner=request.user)[:3]
    if garbages.__len__ == 0:
        return Response(status=status.HTTP_410_GONE)
    else:
        data = []
        for garbage in garbages:
            data.append(garbage.format())
        return Response(data,status=status.HTTP_200_OK)

@api_view(['POST'])
def garbageThrown(request):
    user = User.objects.get(id=request.user.id)
    if(request.data["garbage_id"]):
        garbage:Garbage = get_object_or_404(Garbage,pk=request.data['garbage_id'])
        if(garbage.owner.id == user.id):
            garbage.discard = True
            garbage.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUserThrownGarbage(request):
    user = User.objects.get(id=request.user.id)
    garbages = Garbage.objects.all().filter(owner=user)
    data = []
    for garbage in garbages:
        data.append(garbage.format())
    return Response(data)

@api_view(['POST'])
def postRateGarbage(request):
    user = User.objects.get(id=request.user.id)
    if(request.data['garbage_id'] and request.data['note']):
        garbage:Garbage = get_object_or_404(Garbage,pk=request.data['garbage_id'])
        if garbage.owner != user:
            garbage.addNote(user,int(request.data['note']))
            print("id=" + str(garbage.pk) + " note1=" + str(garbage.ratingJudge1))
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

### Admin functions

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
def deleteAllBins(request):
    Bin.objects.all().delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def deleteAllGarbages(request):
    Garbage.objects.all().delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def setAllBinValid(request):
    bins = Bin.objects.all()
    for bin in bins:
        bin.isAccepted = True
        bin.isVerified = True
        bin.save()
    return Response(status=status.HTTP_200_OK)