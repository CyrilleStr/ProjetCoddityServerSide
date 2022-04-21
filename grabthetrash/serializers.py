from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('pk','isBin','owner', 'isVerified', 'isAccepted', 'latitude','longitude','image','validator1','validatorVerdict1','validator2','validatorVerdict2','validator3','validatorVerdict3')