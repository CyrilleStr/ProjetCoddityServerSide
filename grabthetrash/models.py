from operator import truediv
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
    latitude = models.FloatField()
    longitude = models.FloatField()

class Garbage(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rate = models.IntegerField(null=True)
    isRatingDone = models.BooleanField(default=False)
    discard = models.BooleanField(default=False)
    judge1 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator1",null=True)
    judge2 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator2",null=True)
    ratingJudge1 = models.IntegerField(null=True)
    ratingJudge2 = models.IntegerField(null=True)

    def isAccepted(self):
        if self.judge1 and self.judge2 and self.judge1:
            if self.ratingJudge1 > 0 and self.ratingJudge2 > 0 and self.ratingJudge3 > 0:
                return True
        return False
    
    def addNote(self,judge:User,note:int):
        if self.judge1 and self.judge2:
            print("Error")
            self.isRatingDone = True
        else:
            if(self.judge1):
                self.judge2 = judge
                self.ratingJudge2 = note
                self.isRatingDone = True
            else:
                self.judge1 = judge
                self.ratingJudge1 = note
            self.save()
    
    def format(self):
        return {
            "id": str(self.id),
            "latitude": str(self.latitude),
            "longitude": str(self.longitude),
            "discard": str(self.discard),
            "accepted" : str(self.isAccepted()),
        }


            

                 