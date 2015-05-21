# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Huodong
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def home(request):
	response = "Welcome to huodong!"
	template = "huodong.html"
	context = {}

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
	huodong_id = get_ref_id()
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
			huodong_type = request.POST["huodong_type"]
			huodong = Huodong(huodong_type=huodong_type)
			huodong.title = request.POST["title"]
			huodong.fee = request.POST["fee"]
			huodong.time = request.POST["time"]
			huodong.location = request.POST["location"]

			huodong.save()

		print Huodong.objects



		questions = request.POST.getlist("question")	
		if questions:
			questions_preview = []
			for question in questions:
				 questions_preview.append(question_table[question])

		print questions_preview


	template = "preview.html"
	context = {
		"type" : huodong_type,
		"title" : huodong.title,
		"fee" : huodong.fee,
		"location" : huodong.location,
		"time" : huodong.time,
		"questions_preview":questions_preview
	}
	return render(request, template, context)



def submit(request):

	huodong_url = "http://127.0.0.1:8000/huodong"
	return HttpResponse("here is your url to share: " + huodong_url )
