from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('pk','owner', 'isAccepted', 'latitude','longitude','image','validator1','validatorVerdict1','validator2','validatorVerdict2','validator3','validatorVerdict3')

class GarbageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garbage
        fields = ('pk','owner', 'isAccepted', 'latitude','longitude','image','validator1','validatorVerdict1','validator2','validatorVerdict2','validator3','validatorVerdict3')