# -*- coding: utf-8 -*-
from django.db import models
# from forms import DictionaryField
# Create your models here.

class Document(models.Model):
	docfile =  models.FileField(upload_to='documents')




# class UserData(models.Model):
#     user = models.ForeignKey(User)
#     meta = DictionaryField(blank=True)


