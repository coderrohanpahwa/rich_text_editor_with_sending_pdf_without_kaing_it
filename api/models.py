from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    content = RichTextField()


    # client=models.OneToOneField(Client,on_delete=models.CASCADE,default=1)
class Vendor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    def __str__(self):
        return self.name
class Client(models.Model):
    name=models.CharField(max_length=100)
    project=models.CharField(max_length=1000)
    post=models.OneToOneField(Post,on_delete=models.CASCADE)

    # send_to=models.ForeignKey(Vendor,on_delete=models.CASCADE,default=0)
# class Project(models.Model):
#     phase=models.CharField(max_length=100)
#     description=models.TextField()
#     timeline=models.CharField(max_length=100)
#     payments=models.IntegerField()
#     send_to=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
class Match(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE,default=0)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE,default=0)
    matched=models.BooleanField(default=False)
    class Meta:
        unique_together=('client','vendor')
    def __str__(self):
        return "Client : "+self.client.name+" and Vendor :"+self.vendor.name
class NumberOfPhases(models.Model):
    macth=models.ForeignKey(Match,on_delete=models.CASCADE,default=0)
    phase=models.CharField(max_length=100,default=0)
    description=models.TextField(default=0)
    timeline=models.CharField(max_length=100,default=0)
    payments=models.IntegerField(default=0)
    # decided_by=models.OneToOneField(Vendor,on_delete=models.CharField,default=0)
    def __str__(self):
        return "Phase : "+self.phase+" Client : "+self.macth.client.name+" Vendor : "+self.macth.vendor.name