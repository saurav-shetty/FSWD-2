from django.db import models

# Create your models here.
class Contact(models.Model):

    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip=models.IntegerField
    
        