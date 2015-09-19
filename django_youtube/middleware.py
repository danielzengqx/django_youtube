# -*- coding: utf-8 -*-
from joins.models import Join

class ReferMiddleware():
	def process_request(self, request):
		#print "here is the request: \n%s" % request
		# try:
		# 	ref_id = request.GET.get("ref", "")
		# except:
		# 	ref_id = False
		ref_id = request.GET.get("ref", "") #request.GET.:A dictionary-like object containing all given HTTP GET parameters, 
											#And .get is a formal function to get the value with the key
		request.session['qr'] = request.GET.get("qr_id", "") 
		request.session['words'] = request.GET.get("words", "") 
		request.session['user'] = request.GET.get("user_id", "")
		try:
			request.session['join_id'] = request.META.get("HTTP_REFERER").split("=")[1]
		except :
			pass
			
		# print "ref_id is %s " % ref_id
		try:
			obj = Join.objects.get(ref_id = ref_id)
			# print obj
		except:
			obj = None

		if obj:
			request.session['ref'] = obj.id
		else:
			request.session['ref'] = ref_id



		# print "huodong_num is %s " % huodong_num


		