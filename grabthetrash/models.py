from ssl import VerifyFlags
from xmlrpc.client import Boolean
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _ 


def imagePath():
        return "default/"

class Bin(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    isVerified = models.BooleanField(null=False,default=False)
    isAccepted = models.BooleanField(null=True)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

class Garbage(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    isRatingDone = models.BooleanField(default=False)
    rate = models.IntegerField(null=True)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    judge1 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator1",null=True)
    judge2 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator2",null=True)
    judge3 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator3",null=True)
    ratingJudge1 = models.IntegerField(null=True)
    ratingJudge2 = models.IntegerField(null=True)
    ratingJudge3 = models.IntegerField(null=True)