from django.shortcuts import render
from django.http import HttpResponse
from models import Huodong

# Create your views here.
def preview(request):
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

	template = "preview.html"
	context = {
		"type" : huodong_type,
		"title" : huodong.title,
		"fee" : huodong.fee,
		"location" : huodong.location,
		"time" : huodong.time,
	}
	return render(request, template, context)

def home(request):
	response = "Welcome to huodong!"
	template = "huodong.html"
	context = {}

	return render(request, template, context)

