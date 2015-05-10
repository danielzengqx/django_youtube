from django.shortcuts import render





def testhome(request):
	context = {}
	template = "home.html"

	return render(request,template, context)


def weixin(request):
	context = {}
	template = "share.html"

	return render(request,template, context)

