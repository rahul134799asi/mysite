from __future__ import unicode_literals
from django.db import models


class Company(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=300)


    def __unicode__(self):
        return "{}".format(self.Name)

class Users(models.Model):
    Name = models.CharField(max_length=200)
    Role = models.CharField(max_length=100)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)


    def __unicode__(self):
        return "{}".format(self.Name)






