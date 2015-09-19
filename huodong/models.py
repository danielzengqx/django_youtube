from django.db import models

# Create your models here.
from mongoengine import *
from django_youtube.settings import DBNAME

connect(DBNAME)

class  Huodong(Document):
	# huodong_id = StringField(max_length=120, unique=True)
	# huodong_type = StringField(max_length=120, required=True)
	# title = StringField(max_length=100, required=True)
	# fee = StringField(max_length=500, required=True)
	# # time = DateTimeField(required=True)
	# time = StringField(max_length=500, required=True)
	# location = StringField(max_length=500, required=True)
	huodong_id	= StringField(max_length=10)
	all_content = DictField()
	def __unicode__(self):
		return "%s" % (self.huodong_id)


class Info(Document):
	join_id = StringField(max_length=10)
	q_a = ListField()
	def __unicode__(self):
		return "%s" % (self.join_id)


class UserHuodong(Document):
	#wechat_id is encripted by wechat
	user_id = StringField(max_length=50)
	#all_huodong is a list contains all of the huodong_id for this User
	all_huodong = ListField() 
	def __unicode__(self):
		return "%s" % (self.wechat_id)
