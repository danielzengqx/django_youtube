# -*- coding: utf-8 -*-
# coding=gbk
from django.conf import settings 
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from models import Huodong, Info
import sys
from django.core.cache import cache
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])


# Create your views here.
def home(request):
	response = "Welcome to huodong!"
	template = "huodong.html"
	context = {}
	# for obj in  Huodong.objects.all():
	# 	print "content: %s" % obj["all_content"]



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
						'phone_num': '手机',\
						'wechat_num': '微信',\
						'academy': '学院',\
						'major': '专业',\
						'sex': '性别'}

	if request.method == 'POST':
		# for key, value in request.POST.iteritems():
		# 	print key + ":" + value

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
	notice = OrderedDict([('huodong_type',Type), ('title', Title), ('fee', Fee), ('location', Location), ('time', Time)])
	all_content = {'huodong_id': huodong_id, 'notice':  notice, 'questions_preview': questions_preview}

	cache.set(huodong_id, all_content, timeout=60)
	a = cache.get(huodong_id)
	
	# for key in  a['notice'].keys():
	# 		print key

	# for value in  a['notice'].values():
	# 		print value

	print "here is cache %s " % cache.get(huodong_id)	

	return render(request, template, context)

def join(request):
	print request
	# try:
	huodong_id = request.session['ref']
	huodong = Huodong.objects.get(huodong_id=huodong_id)
	# print "huodong id is %s\n" % huodong_id
	# print "the obj is %s" % (obj.all_content)
		# print "friends recommended by %s are as followed:" % obj
		# print Join.objects.filter(friend=obj).count()
		# print obj.referral.all().count()

	# except:
	# 	obj = None

	notice = huodong.all_content['notice']
	questions = huodong.all_content['questions_preview']
	template = 'join.html'
	context = {
		"type" : notice['huodong_type'],
		"title" : notice['title'],
		"fee" : notice['fee'],
		"location" : notice['location'],
		"time" : notice['time'],
		"questions_preview" : questions
		# 'ref_url': ref_url
		#'huodong_type': all_content['notice'].pop('活动类型'),
		# 'notices' : all_content['notice'],
		# "questions" : all_content['questions_preview']
	}
	return render(request, template, context)
	# return HttpResponse("here is hudong id %s" % all_content['notice']['huodong_type'])

# def process_before_preview(request):
# 	question_table = {\
# 						'user_name': '姓名',\
# 						'phone_num': '手机号码',\
# 						'wechat_num': '微信号',\
# 						'academy': '学院',\
# 						'major': '专业',\
# 						'sex': '性别'}

# 	if request.method == 'POST':
# 		for key, value in request.POST.iteritems():
# 			print key + ":" + value

# 		if request.POST.iteritems():
# 			Type = request.POST["huodong_type"]
# 			Title = request.POST["title"]
# 			Fee = request.POST["fee"]
# 			Time = request.POST["time"]
# 			Location = request.POST["location"]

# 		questions = request.POST.getlist("question")
# 		if questions:
# 			questions_preview = []
# 			for question in questions:
# 				 questions_preview.append(question_table[question])

# 		print questions_preview
	
# 	huodong_id = get_ref_id()
# 	cache.set(huodong_id, questions_preview, timeout=60)

# 	#print "here is cache %s " % cache.get(huodong_id))
# 	return HttpResponseRedirect("/huodong/preview/%s" % huodong_id)


def release(request, huodong_id):
	all_content = cache.get(huodong_id)
#	if request.method == 'POST':
	# print "here is all content %s: " % all_content
#		for key, value in request.POST.iteritems():
#			print key + ":" + value
	# huodong_type = request.POST["huodong_type"]
	# huodong = Huodong(Type=huodong_type)
	# print "daniel huodong id %s : " % huodong.huodong_id
	# huodong.title = request.POST["title"]
	# huodong.fee = request.POST["fee"]
	# huodong.time = request.POST["time"]
	# huodong.location = request.POST["location"]

	try:
		huodong = Huodong.objects.get(huodong_id=huodong_id)

	except:
		# huodong.huodong_id = huodong_id
		huodong = Huodong(huodong_id)
		huodong.all_content = all_content
		huodong.save()

	ref_url = settings.SHARE_URL + str(huodong_id)
	# print Huodong.objects

	template = "share_huodong.html"
	context = {
		# "type" : Type,
		# "title" : Title,
		# "fee" : Fee,
		# "location" : Location,
		# "time" : Time,
		# "questions_preview":questions_preview
		'ref_url': ref_url
		#'huodong_type': all_content['notice'].pop('活动类型'),
		#'notices' : all_content['notice'],
		#"questions" : all_content['questions_preview']
	}
	return render(request, template, context)
	#return HttpResponse("Here is your cache: %s" %  unicode(cache.get(huodong_id)))

def submit(request):

	huodong_url = "http://127.0.0.1:8000/huodong"
	return HttpResponse("here is your url to share: " + huodong_url )


def success(request):
	all_q_a = {}
	# print request
	if request.session['join_id']:
		join_id = request.session['join_id']
	# 	print "join id is %s \n" % request.session['join_id']
	# else:
	# 	print "no join id\n"

	if request.method == "POST":
		# print request.POST
		q_a = dict(request.POST.iteritems())   #.iteritems() returns a generator object so q_a is a generator.Generator will generate values only once. After that it will be empty
		del q_a[u'csrfmiddlewaretoken']
	try:
		info = Info.objects.get(join_id=join_id)
		print "hre is origin q_a: %s" % info.q_a 
		info.q_a.extend([q_a])
		info.save()

	except:
		info = Info(join_id)
		info.q_a = [q_a]
		info.save()




	# info = Info.objects.get(join_id=join_id)
	# for k, v in q_a.items():
	# 	print k, v

	with open("join_report.txt", "a") as f:
		f.writelines(50 * "*" + "\n")
		for k, v in q_a.items():
			f.writelines(k +  (30 - len(k)) * " " + ":     " + v + "\n")



	# except:
	# 	info_save = Info.objects.get(join_id=join_id)

	# 	print info_save

	# for q_a in info_save.q_a:
	# 	print q_a

	return	HttpResponse("提交成功！")




















