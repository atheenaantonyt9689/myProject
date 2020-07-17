from __future__ import unicode_literals
from django.db import models

class Userdetails(models.Model):
    userid = models.EmailField(max_length=35, primary_key=True)
    password=models.CharField(max_length=20)
    conformpassword=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20 )
    middle_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth=models.CharField(max_length=10)
    contact_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    nation=models.CharField(max_length=30)
    profession=models.CharField(max_length=30)

class Login(models.Model):
    userid = models.EmailField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=20)


# Create your models here.




class Legalofficer(models.Model):
    userid = models.EmailField(max_length=20, primary_key=True)
    full_name = models.CharField(max_length=35)
    professional_summary = models.CharField(max_length=500)
    core_qualification = models.CharField(max_length=200)
    practice = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)

class Medicalofficer(models.Model):
    userid = models.EmailField(max_length=20, primary_key=True)
    full_name = models.CharField(max_length=35)
    professional_summary = models.CharField(max_length=500)
    core_qualification = models.CharField(max_length=200)
    practice = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)

class Customsofficer(models.Model):
    userid = models.EmailField(max_length=20, primary_key=True)
    full_name = models.CharField(max_length=35)
    professional_summary = models.CharField(max_length=500)
    core_qualification = models.CharField(max_length=200)
    practice = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)

class Narcoticofficer(models.Model):
    userid = models.EmailField(max_length=20, primary_key=True)
    full_name = models.CharField(max_length=35)
    professional_summary = models.CharField(max_length=500)
    core_qualification = models.CharField(max_length=200)
    practice = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)

class Socialworker(models.Model):
    userid = models.EmailField(max_length=20, primary_key=True)
    full_name = models.CharField(max_length=35)
    professional_summary = models.CharField(max_length=500)
    core_qualification = models.CharField(max_length=200)
    practice = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)

class Event(models.Model):
    name = models.CharField(max_length=30)
    event_date = models.DateTimeField(max_length=20)
    venue = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    description = models.CharField(max_length=100)




























