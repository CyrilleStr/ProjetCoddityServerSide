from ssl import VerifyFlags
from xmlrpc.client import Boolean
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _ 

class Item(models.Model):
    def imagePath():
        return "default/"

    isBin = models.BooleanField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    isVerified = models.BooleanField(null=False,default=False)
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

    def refreshIsAccepted(self):
        if self.validator1 and self.validator2 and self.validator3:
            self.isVerified = True
            if self.validatorVerdict1 and self.validatorVerdict2 and self.validatorVerdict3:
                self.isAccepted = True
            else:
                self.isAccepted = False
        else: 
            self.isVerified = False
        return self.isAccepted

    def addVerdict(self, validator:User,verdict:Boolean):
        if self.validator1 is None:
            self.validator1 = validator
            self.validatorVerdict1 = verdict
            return True;
        elif self.validator2 is None:
            self.validator2 = validator
            self.validatorVerdict2 = verdict
            return True;
        elif self.validator3 is None:
            self.validator3 = validator
            self.validatorVerdict3 = verdict
            self.refreshIsAccepted()
            return True;
        else:
            return False;