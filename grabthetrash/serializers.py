from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = (
            'owner',
            'isVerified', 
            'isAccepted', 
            'latitude',
            'longitude',
            'image',
        )

class BinCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = (
            "owner",
            "latitude",
            "longitude",
        )

class GarbageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garbage
        fields = (
            'owner',
            'isRatingDone', 
            'latitude',
            'longitude',
            'image',
            'judge1',
            'ratingJudge1',
            'judge2',
            'ratingJudge2',
            'judge3',
            'ratingJudge3',
        )

