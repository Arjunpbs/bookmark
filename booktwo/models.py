# models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bookstore(models.Model):
    bid=models.AutoField
    bname=models.CharField(max_length=500)
    auther=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    nationality=models.CharField(max_length=200)
    coverpic=models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.bname

class Bookshelf(models.Model):
    book_id=models.AutoField
    book_name=models.CharField(max_length=500)
    book_auther=models.CharField(max_length=500)
    book_genre=models.CharField(max_length=100)
    book_nationality=models.CharField(max_length=200)
    book_link=models.CharField(max_length=500)
    book_coverpic=models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.book_name

class  review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=100)
    rating = models.IntegerField()
    
