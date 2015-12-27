from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def home(request):
	user_id = request.session['user']
	response = "Welcome to yearbook!"
	template = "yearbook.html"
	context = {
		'user_id' : user_id
	}
	# for obj in  Huodong.objects.all():
	# 	print "content: %s" % obj["all_content"]


	# return HttpResponse(response)
	return render(request, template, context)
