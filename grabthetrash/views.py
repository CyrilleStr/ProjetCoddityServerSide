from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from grabthetrash.serializers import *
from .models import *

class ItemCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, format=None):
        print(request.data)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(['GET'])
def getItemsToValidate(request):
    items = Item.objects.all().filter(isAccepted=False)[:3]
    itemSerializer = ItemSerializer(items,many=True)
    if items.__len__ == 0:
        return Response(itemSerializer.errors, status=status.HTTP_410_GONE)
    else:
        return Response(itemSerializer.data)

@api_view(['POST'])
def itemsValidation(request):
    user = User.objects.get(id=request.user.id)
    if request.POST['pk1'] and request.POST['pk2'] and request.POST['pk3'] and request.POST['answer1'] and request.POST['answer2'] and request.POST['answer3']:
        if request.POST['pk1'] != "0" :
            item1:Item = get_object_or_404(Item,pk=request.POST['pk1'])
            item1.addVerdict(user,request.POST['answer1'])
            item1.save()
        if request.POST['pk2'] != "0" :
            item2:Item = get_object_or_404(Item,pk=request.POST['pk2'])
            item2.addVerdict(user,request.POST['answer2'])
            item2.save()
        if request.POST['pk3'] != "0" :
            item3:Item = get_object_or_404(Item,pk=request.POST['pk3'])
            item3.addVerdict(user,request.POST['answer3'])
            item3.save()
        
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)