from django.db import models

# Create your models here.
from mongoengine import *
from django_youtube.settings import DBNAME

connect(DBNAME)

class  Huodong(Document):
	huodong_id = StringField(max_length=120, unique=True)
	huodong_type = StringField(max_length=120, required=True)
	title = StringField(max_length=100, required=True)
	fee = StringField(max_length=500, required=True)
	# time = DateTimeField(required=True)
	time = StringField(max_length=500, required=True)
	location = StringField(max_length=500, required=True)

	def __unicode__(self):
		return "%s" % (self.title)
		