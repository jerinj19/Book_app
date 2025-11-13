from django.db import models

class RegisterDb(models.Model):
    Name=models.CharField( max_length=20,null=True,blank=True)
    Email=models.EmailField(max_length=20,null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)
    Confirm_password=models.CharField(max_length=20,null=True,blank=True)

class Contactdb(models.Model):
    Contact_name=models.CharField(max_length=20,null=True,blank=True)
    Contact_email=models.EmailField(max_length=25,null=True,blank=True)
    Contact_phone=models.IntegerField(null=True,blank=True)
    Contact_city=models.CharField(max_length=20,null=True,blank=True)
    Enquiry_type=models.CharField(max_length=20,null=True,blank=True)
    Contact_message=models.TextField(max_length=50,null=True,blank=True)

class Cart(models.Model):
    Book_name=models.CharField(max_length=25,null=True,blank=True)
    username=models.CharField(max_length=30,null=True,blank=True)
    qty=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)
    Book_image=models.ImageField(upload_to="Cart_books",null=True,blank=True)

