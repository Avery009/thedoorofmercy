from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
# Create your views here.

def home(request):
	template = loader.get_template('home/home.html')
	#extract authenticated user to pass to home.html
	#if request.user.is_authenticated:
	#	user = request.user
	user = 'James'
	context = {
		'user' : user
	}
	return HttpResponse(template.render(context,request))

