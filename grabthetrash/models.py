from tkinter import CASCADE
from tokenize import String
from django.contrib.auth.models import User
from django.db import models

class Coordinate(models.Model):
    longitude = models.IntegerField()
    latitude = models.IntegerField()

class Validation(models.Model):
    validator = models.ForeignKey(User,on_delete=models.CASCADE)
    isValid = models.BooleanField()

class ThirdPratValidationObject(models.Model):
    imagePath:String = "img/default/"
    
    # Database model
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    isAccepted = models.BooleanField()
    location = models.ForeignKey(Coordinate,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=imagePath)
    thirdPartValidation1 = models.ForeignKey(Validation,on_delete=models.CASCADE,related_name="thirdPartValidation1")
    thirdPartValidation2 = models.ForeignKey(Validation,on_delete=models.CASCADE,related_name="thirdPartValidation2")
    thirdPartValidation3 = models.ForeignKey(Validation,on_delete=models.CASCADE,related_name="thirdPartValidation3")

    def refreshIsValid(self):
        if self.thirdPartValidation1 and self.thirdPartValidation1 and self.thirdPartValidation1:
            if self.thirdPartValidation1.isValid and self.thirdPartValidation1.isValid and self.thirdPartValidation1.isValid:
                self.isAccepted = True
            self.isAccepted = False
        else: 
            self.isAccepted = False
        return self.isAccepted

class Bin(ThirdPratValidationObject):
    imagePath = "img/bin/"

class Garbage(ThirdPratValidationObject):
    imagePath = "img/garbage/"