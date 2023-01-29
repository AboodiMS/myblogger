from django.db import models

# Create your models here.

class Cover(models.Model):
    titel=models.CharField(max_length=255)
    details=models.CharField(max_length=255)

class Profile(models.Model):
    fullname=models.CharField(max_length=255)
    birthday=models.CharField(max_length=255)
    livingin=models.CharField(max_length=255)
    university=models.CharField(max_length=255)
    college=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    yearofgraduation=models.CharField(max_length=255)

class Skill(models.Model):
    skillname=models.CharField(max_length=255)

class ExCompany(models.Model):
    companyname=models.CharField(max_length=255)
    jobtitle=models.CharField(max_length=255)
    details=models.CharField(max_length=1000)

class Portifolio(models.Model):
    projecttitel=models.CharField(max_length=255)
    tools=models.CharField(max_length=255)
    details=models.CharField(max_length=1000)

class Message(models.Model):
    email=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    message=models.CharField(max_length=1000)

