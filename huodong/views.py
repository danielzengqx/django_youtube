# -*- coding: utf-8 -*-
# coding=gbk
# from __future__ import absolute_import

from django.conf import settings 
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from models import Huodong, Info, UserHuodong
import sys
from django.core.cache import cache
from collections import OrderedDict
import qrcode
import csv

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])


# Create your views here.
def home(request):
	user_id = request.session['user']
	response = "Welcome to huodong!"
	template = "huodong.html"
	context = {
		'user_id' : user_id
	}
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
	user_id = request.session['user']
	print "here is user_id %s" % user_id
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
		"user_id" : user_id,
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


def release(request, user_id, huodong_id):
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
		if request.GET['from'] == u'singlemessage':
				new_url = settings.SHARE_URL + request.path.split('/')[-1]
				print request.GET
				return HttpResponseRedirect(new_url)
	except:
		pass


	try:
		huodong = Huodong.objects.get(huodong_id=huodong_id)

	except:
		# huodong.huodong_id = huodong_id
		huodong = Huodong(huodong_id)
		huodong.all_content = all_content
		huodong.save()



	ref_url = settings.SHARE_URL + str(huodong_id)
	#Generate QR image
	# print 'here is static path: %s' % settings.STATICFILES_DIRS + 'img'
	# print 'here is type: %s' % type(settings.STATICFILES_DIRS[0])
	qr_path = settings.STATICFILES_DIRS[0] +'/img/' +str(huodong_id) +'.png'
	print qr_path
	qr_url = "http://127.0.0.1/" + qr_path
	print qr_url
	# print "daniel, here is qr: %s" % qr_path
	gen_qr(ref_url, qr_path)

	# print Huodong.objects

	#Put this huodong_id in to UserHuodong db.
	try:
		user_huodong = UserHuodong.objects.get(user_id=user_id)

	except:
		# huodong.huodong_id = huodong_id
		user_huodong = UserHuodong(user_id)
	
	# print "here is origin all huodongs" + 50*"="
	# print user_huodong.all_huodong
	if huodong_id not in user_huodong.all_huodong:
		user_huodong.all_huodong.append(huodong_id)
	user_huodong.save()

	# print "here is after all huodongs" + 50*"*"
	# print user_huodong.all_huodong

	release_file = huodong_id + '.csv'

	print all_content['questions_preview']

	with open(release_file, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(all_content['questions_preview'])

	template = "share_huodong.html"
	context = {
		# "type" : Type,
		# "title" : Title,huo
		# "fee" : Fee,
		# "location" : Location,
		# "time" : Time,
		# "questions_preview":questions_preview
		'ref_url': ref_url,
		'huodong_id': str(huodong_id)
		#'huodong_type': all_content['notice'].pop('活动类型'),
		#'notices' : all_content['notice'],
		#"questions" : all_content['questions_preview']
	}
	# print "daniel, huodong_id: " + str(huodong_id)
	return render(request, template, context)
	#return HttpResponse("Here is your cache: %s" %  unicode(cache.get(huodong_id)))

def submit(request):

	huodong_url = "http://www.xiaoxiezi.net/huodong"
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
	huodong_file = join_id + '.csv'

	if os.path.isfile(huodong_file):
		print "file exists *" + 50*"*"
		with open(huodong_file, 'ab') as f:	
			row_a = list()
			writer = csv.writer(f)
			print "here is q_a:" + 50*"*"
			print q_a.items()
			for k, v in q_a.items():
				row_a.append(v)
			writer.writerow(row_a)

	else:
		print "file no exists " + 50*"-"
		with open(huodong_file, 'wb') as f:	
			row_q = list()
			row_a = list()
			writer = csv.writer(f)

			# writer.writerow(all_content['questions_preview'])
			for k, v in q_a.items():
				row_q.append(k)
				row_a.append(v)
			writer.writerow(row_q)
			writer.writerow(row_a)

	# with open(huodong_file, "a") as f:
	# 	f.writelines(50 * "*" + "\n")
	# 	for k, v in q_a.items():
	# 		f.writelines(k +  (30 - len(k)) * " " + ":     " + v + "\n")



	# except:
	# 	info_save = Info.objects.get(join_id=join_id)

	# 	print info_save

	# for q_a in info_save.q_a:
	# 	print q_a

	# return	HttpResponse("提交成功！")



	template = "success.html"
	context = {
		# 'user_id' : user_id,
		# 'id_titles' : id_titles,

	}

	return render(request, template, context)


# from django.utils.encoding import smart_str

import os
from django.core.servers.basehttp import FileWrapper


def write_csv(request):
	# Create the HttpResponse object with the appropriate CSV header.
	file = request.session['file']
	path = os.getcwd()
	# file = path + '/02adc9a4d3.csv'
	print path
	wrapper = FileWrapper(open( file, "r" )	)
	response = HttpResponse(wrapper, content_type='text/csv')
	response.write('\xEF\xBB\xBF')
	response['Content-Disposition'] = 'attachment; filename="' + file + '"'
	return response


def mine(request):
	user_id = request.session['user']
	print "here is my wechat id: %s" % user_id	

	try:
		user_huodong = UserHuodong.objects.get(user_id=user_id)

	except:
		print "some thing wrong with user_id*****************\n"

	huodongs = user_huodong.all_huodong

	print "here is all huodongs" + 50*"="
	print huodongs

	id_titles = OrderedDict()
	for id in huodongs :
		huodong = Huodong.objects.get(huodong_id=id)
		id_titles[id] = huodong.all_content['notice']['title']

	print "here is huodong title %s" % id_titles

	template = "mine.html"
	context = {
		'user_id' : user_id,
		'id_titles' : id_titles,

	}

	
	# return HttpResponse(user_id + '\n' +str(huodongs))
	return render(request, template, context)


def gen_qr(url, path):	
	qr = qrcode.QRCode(
	    version=1,
	    error_correction=qrcode.constants.ERROR_CORRECT_L,
	    box_size=10,
	    border=4,
	)
	qr.add_data(url)
	qr.make(fit=True)

	img = qr.make_image()
	# img.save('/Users/daniel/daniel_code/project_mysite/django_youtube/static/static_dirs/img/daniel.png')
	img.save(path)





def qr(request):
	qr_id = request.session['qr']
	words = request.session['words']
	print "daniel, here is words: %s" % words
	# words = 'Welcome to my world!!'
	qr_path = settings.STATICFILES_DIRS[0] +'/img/' +str(qr_id) +'.png'
	# print "daniel, here is qr: %s" % qr_path
	gen_qr(words, qr_path)

	# print Huodong.objects

	template = "qr_zone.html"
	context = {
		'qr_id': str(qr_id)
	}
	return render(request, template, context)
	#return HttpResponse("Here is your cache: %s" %  unicode(cache.get(huodong_id)))





import requests
def douban(request):
	url = r'http://book.douban.com/chart?icn=index-topchart-nonfiction'
	r = requests.get(url)
	return HttpResponse(r.text)




