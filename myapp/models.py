from email.policy import default
from django.db import models

# Create your models here.

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50,default="")
    role = models.CharField(max_length=50,default=0)
   
    
    

class Admin(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE,default="")
    role = models.CharField(max_length=50,default="Admin")
    email = models.EmailField(max_length=100,default="")
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
    
class Student(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE,default="")
    role = models.CharField(max_length=50,default="Student")
    email = models.EmailField(max_length=100,default="")
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
        
    

class Book(models.Model):
    bname = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    
    
    
