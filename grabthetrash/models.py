from tkinter import CASCADE
from tokenize import String
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _ 

class ThirdPartValidationObject(models.Model):
    def imagePath():
        return "default/"

    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    isAccepted = models.BooleanField(null=True)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    image = models.ImageField(_("Image"),upload_to=imagePath(), default='defaults.jpg')
    validator1 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator1",null=True)
    validatorVerdict1 = models.BooleanField(null=True)
    validator2 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator2",null=True)
    validatorVerdict2 = models.BooleanField(null=True)
    validator3 = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="validator3",null=True)
    validatorVerdict3 = models.BooleanField(null=True)

    def refreshIsValid(self):
        if self.validatorId1 and self.validatorId2 and self.validatorId3:
            if self.validatorVerdict1 and self.validatorVerdict2 and self.validatorVerdict3:
                self.isAccepted = True
            else:
                self.isAccepted = False
        else: 
            self.isAccepted = None
        return self.isAccepted

class Bin(ThirdPartValidationObject):

    def imagePath():
        return "bin/"

class Garbage(ThirdPartValidationObject):
    def imagePath():
        return "garbage/"