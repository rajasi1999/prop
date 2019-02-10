from django.db import models
from django.contrib.auth.models import User
from . import choices
# Create your models here.
class College(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    name = models.CharField(max_length = 255, blank = False)
    college_code = models.CharField(max_length = 8, blank = False)
    college_address = models.TextField(blank = True, null = True)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    college_name = models.CharField(max_length = 128)

class Government(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    city = models.CharField(max_length = 100,blank = False)
    officer_name = models.CharField(max_length = 128,blank = False)

class Form(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    from_station = models.CharField(max_length = 20)
    to_station = models.CharField(max_length = 20)
    pass_type = models.CharField(max_length = 10 , choices = choices.PASS_TYPE, default = "SECOND CLASS")
    sap_id = models.CharField(max_length = 11 ,blank = False)
    address = models.CharField(max_length = 255)
