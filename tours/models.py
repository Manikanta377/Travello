from django.db import models

class Destination(models.Model):
   
    name= models.CharField(max_length=50)
    description= models.TextField()
    price= models.IntegerField()
    image= models.ImageField(upload_to='pics')
    days= models.CharField()
    offer= models.BooleanField(default=False)
