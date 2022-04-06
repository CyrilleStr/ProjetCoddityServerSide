from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('owner', 'isAccepted', 'location','image','thirdPartValidation1','thirdPartValidation2','thirdPartValidation3')

class GarbageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garbage
        fields = ('owner', 'isAccepted', 'location','image','thirdPartValidation1','thirdPartValidation2','thirdPartValidation3')
        