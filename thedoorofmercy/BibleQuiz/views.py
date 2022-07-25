from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Sermon
from .forms import forms
from django.template import loader
import datetime

def biblequiz(request):
	#Load completed and current as separate lists
	#sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
	template = loader.get_template('/biblequiz/biblequiz.html')
	context = {
		#'sermon_list' : sermon_list,
	}
	return HttpResponse(template.render(context,request))
def enterbiblequiz(request):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/biblequiz/biblequiz.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
def viewbiblequiz(request, biblequiz_id):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/biblequiz/biblequiz.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
def editbiblequiz(request, biblequiz_id):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/biblequiz/biblequiz.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
def removebiblequiz(request, biblequiz_id):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/biblequiz/biblequiz.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
