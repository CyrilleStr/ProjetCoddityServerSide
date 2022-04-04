from rest_framework import serializers
from django.contrib.auth.models import User
# import model from models.py
from .models import Tips
 
# Create a model serializer
class TipsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Tips
        fields = ('title', 'description')
