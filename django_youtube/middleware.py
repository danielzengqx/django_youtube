from joins.models import Join

class ReferMiddleware():
	def process_request(self, request):
		#print "here is the request: \n%s" % request
		# try:
		# 	ref_id = request.GET.get("ref", "")
		# except:
		# 	ref_id = False
		ref_id = request.GET.get("ref", "")
		#print ref_id
		try:
			obj = Join.objects.get(ref_id = ref_id)
			# print obj
		except:
			obj = None

		if obj:
			request.session['ref'] = obj.id



		