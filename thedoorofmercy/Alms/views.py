from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Sermon
from .forms import forms
from django.template import loader
import datetime

def alms(request):
	#Load completed and current as separate lists
	#sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
	template = loader.get_template('/alms/alms.html')
	context = {
		#'sermon_list' : sermon_list,
	}
	return HttpResponse(template.render(context,request))
def enteralms(request):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/alms/alms.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
def viewalms(request, alms_id):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/alms/alms.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
def editalms(request, alms_id):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/alms/alms.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
def removealms(request, alms_id):
	#Load completed and current as separate lists
        #sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
        template = loader.get_template('/alms/alms.html')
        context = {
                #'sermon_list' : sermon_list,
        }
        return HttpResponse(template.render(context,request))
