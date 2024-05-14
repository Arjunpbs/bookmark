from django.db import models

# Create your models here.
class Contactus(models.Model):
    name=models.CharField(max_length=50)
    phoneno=models.IntegerField()
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=700)
    def __str__(self):
        return self.name
    
