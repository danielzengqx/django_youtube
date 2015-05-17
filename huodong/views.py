from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
	response = "Welcome to huodong!"
	template = "huodong.html"
	context = {}

	return render(request, template, context)