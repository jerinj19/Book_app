from django.db import models

class Book_category(models.Model):
    Category_name=models.CharField(max_length=20,null=True,blank=True)
    Category_description=models.TextField(max_length=50,null=True,blank=True)
    Category_image=models.ImageField(upload_to="category_images",null=True,blank=True)
class Book(models.Model):
    Book_Tittle=models.CharField(max_length=20,null=True,blank=True)
    Book_author=models.CharField(max_length=25,null=True,blank=True)
    Category=models.CharField(max_length=10,null=True,blank=True)
    Book_Price=models.IntegerField(null=True,blank=True)
    Book_Publisher=models.CharField(null=True,blank=True)
    Book_Description=models.TextField(max_length=50,null=True,blank=True)
    Book_image=models.ImageField(upload_to="book images",null=True,blank=True)