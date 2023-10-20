from django.db import models

# Create your models here.
class contactform(models.Model):
    Name=models.CharField(max_length=50)
    Contact=models.IntegerField()
    People=models.IntegerField()
    Message=models.CharField(max_length=500)
