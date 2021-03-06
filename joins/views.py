# -*- coding: utf-8 -*-

# Create your views here.
from django.conf	import settings 
from django.shortcuts import render, HttpResponseRedirect, Http404


from .forms import EmailForm, JoinForm
from .models import Join

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
import hashlib
from huodong.views import gen_qr 

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
				ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")

	except:	
		ip = ""

	return ip

import uuid

def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id


def share(request, ref_id):
	#print ref_id
	try:
		print "here is ref_id : %s" % ref_id
		join_obj = Join.objects.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		count = join_obj.referral.all().count()
		ref_url = settings.SHARE_URL + str(join_obj.ref_id)
		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request,template, context)
	except:
		print "daniel here is wrong ref_id: %s" %ref_id
		raise	Http404

def home(request):
	#	print request.POST['email']
	# form = EmailForm(request.POST or None)

	#This is using regular django forms
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print new_join, created
	# 	print new_join.timestamp 
	# 	if created:
	# 			print "This obj was created"
	#this is using model forms

	try:
		join_id = request.session['ref']
		obj = Join.objects.get(id=join_id)

		print "the obj is %s" % (obj.email)
		print "friends recommended by %s are as followed:" % obj
		print Join.objects.filter(friend=obj).count()
		print obj.referral.all().count()

	except:
		obj = None


	form = JoinForm(request.POST or None)

	if form.is_valid():
			new_join = form.save(commit=False)
	 		#we might do something here
	 		email = form.cleaned_data['email']
	 		#get_or_created can avoid create the same Join.and the ModelForm.save() can't do that.
			new_join_old, created = Join.objects.get_or_create(email=email)  
	 		if created:
				new_join_old.ref_id = get_ref_id()
				# add our friend who referred us to our join model or a related .
				if not obj == None:
					new_join_old.friend = obj
				new_join_old.ip_address = get_ip(request)
				new_join_old.save() 

			#print all "friends" that joined as a result of main sharer email



			#redirect here
			return HttpResponseRedirect("/%s" % new_join_old.ref_id)

			#new_join.save()
	print form
	context = {"form": form}
	template = "home.html"


	return render(request,template, context)


def checkSignature(request):
    signature = request.GET.get('signature',None)
    timestamp = request.GET.get('timestamp',None)
    nonce = request.GET.get('nonce',None)
    echostr = request.GET.get('echostr',None)
    
    token = "danieltoken"

    tmplist = [token,timestamp,nonce]
    tmplist.sort()
    tmpstr = "%s%s%s"%tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echostr
    else:
        return None

def autoReply(request):
	str_xml = web.data() #get post data 
	xml = etree.fromstring(str_xml) #parse xml 
   	content = xml.find("Content").text # get user input content
	msgType = xml.find("MsgType").text
	fromUser = xml.find("FromUserName").text
	toUser = xml.find("ToUserName").text
	return self.render.reply_text(fromUser,toUser,int(time.time()),u"I'm still in developing, what you typed are:"+content)

@csrf_exempt
def weixin(request):
	try:
	    if request.method == 'GET':
	    	print request
	       	response = HttpResponse(checkSignature(request))
	       	return response

	    elif request.method ==  'POST':
	    	print "daniel ,here is post!"
	    	print request.body
	    	str_xml = request.body #get post data 
	    	xml = etree.fromstring(str_xml) #parse xml
	    	print xml


	    	msgType = xml.find("MsgType").text
	    	fromUser = xml.find("FromUserName").text
	    	toUser = xml.find("ToUserName").text
	    	#return self.render.reply_text(fromUser,toUser,int(time.time()),u"I'm still in developing, what you typed are:"+content)
	    	#return autoReply(request)

		if msgType == "event":
			event = xml.find("Event").text
	    		rawContent = "你好，欢迎关注小鞋子\n发送任意字符\n创建《我的2015》,\n每次发送会重新生成配置页面>_< \n\n--- 小鞋子(1129321939)"
	    		content = unicode(rawContent, "utf-8")
		    	response = "<xml>\
							<ToUserName><![CDATA[" + fromUser +"]]></ToUserName>\
							<FromUserName><![CDATA[" + toUser + "]]></FromUserName>\
							<CreateTime>1431255793</CreateTime>\
							<MsgType><![CDATA[text]]></MsgType>\
							<Content><![CDATA[" + content + "]]></Content>\
							</xml>"	    	
		else:
			yearbook_id = get_ref_id()			
			vl_pic_url1 = "http://a3.qpic.cn/psb?/V117jtH93YWWiG/Ww1ZkeceACvL6Vv.2i*RWwf0fg0UBPnJR6qDtkm9.vM!/b/dFsBAAAAAAAA&bo=XgOAAgAAAAAFAPw!&rf=viewer_4&t=5"
			vl_pic_url = "http://a3.qpic.cn/psb?/V117jtH93YWWiG/Ww1ZkeceACvL6Vv.2i*RWwf0fg0UBPnJR6qDtkm9.vM!/b/dFsBAAAAAAAA&bo=XgOAAgAAAAAFAPw!&rf=viewer_4&t=5"
	    		#content = unicode(rawContent, "utf-8")
			vl_url1 = "http://www.xiaoxiezi.net/huodong/yearbook/" + yearbook_id
			vl_url = "http://www.xiaoxiezi.net/huodong/yearbook/" + yearbook_id

			vl_title1 = "我的2015"
			vl_description1 = "我的2015"
			vl_title = "我的2015"
			vl_description = "我的2015"

			response = "<xml>\
                                <ToUserName><![CDATA[" + fromUser + "]]></ToUserName>\
                                <FromUserName><![CDATA[" + toUser + "]]></FromUserName>\
                                <CreateTime>12345678</CreateTime>\
                                <MsgType><![CDATA[news]]></MsgType>\
                                <ArticleCount>2</ArticleCount>\
                                <Articles>\
                                <item>\
                                <Title><![CDATA[" + vl_title1 + "]]></Title> \
                                <Description><![CDATA[" + vl_description1 + "]]></Description>\
                                <PicUrl><![CDATA[" + vl_pic_url1 + "]]></PicUrl>\
                                <Url><![CDATA[" + vl_url1 + "]]></Url>\
                                </item>\
                                <item>\
                                <Title><![CDATA[" + vl_title + "]]></Title>\
                                <Description><![CDATA[" + vl_description + "]]></Description>\
                                <PicUrl><![" + vl_pic_url + "]]></PicUrl>\
                                <Url><![CDATA[" + vl_url + "]]></Url>\
                                </item>\
                                </Articles>\
                                </xml>"
			

	    	return HttpResponse(response)
	    else:
	    	print "here is else %s" % request
	        return HttpResponse('Hello World')

	except Exception, error: #to print the error
		print error

def kindle(request):
	context = {}
	template = 'kindleren_summary.html'
	return render(request, template, context)
	

