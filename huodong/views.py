# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from models import Huodong
import sys
from django.core.cache import cache
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def home(request):
	response = "Welcome to huodong!"
	template = "huodong.html"
	context = {}
	print "my cache %s" % cache.get("7b5e160661")
	return render(request, template, context)

import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id

def preview(request):

	question_table = {\
						'user_name': '姓名',\
						'phone_num': '手机号码',\
						'wechat_num': '微信号',\
						'academy': '学院',\
						'major': '专业',\
						'sex': '性别'}

	if request.method == 'POST':
		for key, value in request.POST.iteritems():
			print key + ":" + value

		if request.POST.iteritems():
			Type = request.POST["huodong_type"]
			Title = request.POST["title"]
			Fee = request.POST["fee"]
			Time = request.POST["time"]
			Location = request.POST["location"]

		questions = request.POST.getlist("question")
		if questions:
			questions_preview = []
			for question in questions:
				 questions_preview.append(question_table[question])

		print questions_preview

	huodong_id = get_ref_id()
	template = "preview.html"
	context = {
		"type" : Type,
		"title" : Title,
		"fee" : Fee,
		"location" : Location,
		"time" : Time,
		"questions_preview":questions_preview,
		"huodong_id": huodong_id
	}
	notice = OrderedDict([('活动类型',Type), ('活动', Title), ('费用', Fee), ('地点', Location), ('时间', Time)])
	all_content = {'huodong_id': huodong_id, 'notice':  notice, 'questions_preview': questions_preview}

	cache.set(huodong_id, all_content, timeout=60)
	a = cache.get(huodong_id)
	
	for key in  a['notice'].keys():
			print key

	for value in  a['notice'].values():
			print value

	print "here is cache %s " % cache.get(huodong_id)	

	return render(request, template, context)

def process_before_preview(request):
	question_table = {\
						'user_name': '姓名',\
						'phone_num': '手机号码',\
						'wechat_num': '微信号',\
						'academy': '学院',\
						'major': '专业',\
						'sex': '性别'}

	if request.method == 'POST':
		for key, value in request.POST.iteritems():
			print key + ":" + value

		if request.POST.iteritems():
			Type = request.POST["huodong_type"]
			Title = request.POST["title"]
			Fee = request.POST["fee"]
			Time = request.POST["time"]
			Location = request.POST["location"]

		questions = request.POST.getlist("question")
		if questions:
			questions_preview = []
			for question in questions:
				 questions_preview.append(question_table[question])

		print questions_preview
	
	huodong_id = get_ref_id()
	cache.set(huodong_id, questions_preview, timeout=60)

	#print "here is cache %s " % cache.get(huodong_id))
	return HttpResponseRedirect("/huodong/preview/%s" % huodong_id)


def release(request, huodong_id):
	all_content = cache.get(huodong_id)
#	if request.method == 'POST':
	print "here is all content %s: " % all_content
#		for key, value in request.POST.iteritems():
#			print key + ":" + value
	# huodong_type = request.POST["huodong_type"]
	# huodong = Huodong(Type=huodong_type)
	#huodong.huodong_id = get_ref_id()
	# print "daniel huodong id %s : " % huodong.huodong_id
	# huodong.title = request.POST["title"]
	# huodong.fee = request.POST["fee"]
	# huodong.time = request.POST["time"]
	# huodong.location = request.POST["location"]

	# huodong.save()

	# print Huodong.objects

	template = "release.html"
	context = {
		# "type" : Type,
		# "title" : Title,
		# "fee" : Fee,
		# "location" : Location,
		# "time" : Time,
		# "questions_preview":questions_preview
		'huodong_type': all_content['notice'].pop('活动类型'),
		'notices' : all_content['notice'],
		"questions" : all_content['questions_preview']
	}
	return render(request, template, context)
	#return HttpResponse("Here is your cache: %s" %  unicode(cache.get(huodong_id)))

def submit(request):

	huodong_url = "http://127.0.0.1:8000/huodong"
	return HttpResponse("here is your url to share: " + huodong_url )
