from django.db import models

class Datalist(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

class Device1(models.Model):
    qrname1= models.TextField(blank = True, null = True)
    namesw1= models.TextField(blank = True, null = True)

class Device2(models.Model):
    qrname2= models.TextField(blank = True, null = True)
    namesw21= models.TextField(blank = True, null = True)
    namesw22= models.TextField(blank = True, null = True)

class Device3(models.Model):
    qrname3= models.TextField(blank = True, null = True)
    namesw31= models.TextField(blank = True, null = True)
    namesw32= models.TextField(blank = True, null = True)
    namesw33= models.TextField(blank = True, null = True)