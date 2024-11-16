from django.db import models

# Create your models here.
class Member(models.Model):
  fullname=models.CharField(max_length=100)
  email=models.EmailField()
  age=models.IntegerField()
  gender=models.CharField(max_length=50)
  yob=models.DateField()

  def __str__(self):
    return self.fullname

class Product(models.Model):
  name=models.CharField(max_length=100)
  price=models.CharField(max_length=50)
  quantity=models.IntegerField()

  def __str__(self):
    return self.name
  

class Appointment(models.Model):
  FullName=models.CharField(max_length=100)
  Email=models.EmailField()
  Phone=models.CharField(max_length=50)
  datetime=models.DateTimeField()
  Department=models.CharField(max_length=50)
  Doctor=models.CharField(max_length=50)
  message=models.TextField()

  def __str__(self):
    return self.FullName

class Contact(models.Model):
  Name=models.CharField(max_length=100)
  Email=models.EmailField()
  Subject=models.CharField(max_length=100)
  Message=models.TextField()

  def __str__(self):
    return self.Subject

