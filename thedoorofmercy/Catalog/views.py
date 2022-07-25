from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Sermon
from .forms import forms
from django.template import loader
import datetime



def sermons(request):
	#Load completed and current as separate lists
	sermon_list = Sermon.objects.all().order_by('sermon_upload_date')
	template = loader.get_template('sermons.html')
	context = {
		'sermon_list' : sermon_list,
	}
	return HttpResponse(template.render(context,request))

def entersermon(request):
	if request.method == 'GET':
		form = forms.SermonEntry()
		context = {
			'form': form,
			'reqGet': True
		}
		template = loader.get_template('sermonform.html')
	elif request.method == 'POST':
		form = forms.SermonEntry(request.POST)
		if form.is_valid():
			sud = datetime.datetime.now()
			st = form.cleaned_data['sermon_title']
			sde = form.cleaned_data['sermon_description']
			sc = form.cleaned_data['sermon_content']
			sa = form.cleaned_data['sermon_author']
			sl = form.cleaned_data['sermon_location']
			
			try:
				s = Sermon(sermon_title=st,sermon_upload_date=sud,sermon_description=sde,sermon_content=sc,sermon_author=sa,sermon_location=sl)
				s.save()
				return redirect('/')
			except Exception as e:
				template = loader.get_template('error.html')
				context = {
					'error' : str(e)
				}
		else:
			context = {		
				'error' : 'Form Validation Error',
			}
			template = loader.get_template('error.html')
	else:
		template = loader.get_template('error.html')
		context = {
			'error' : '501 Invalid Request Protocol',
		}
	return HttpResponse(template.render(context,request))

def viewsermon(request,sermon_id):
	#View an individual testimonial to pray for it
	if request.method == 'GET':
		try:
			sermon = Sermon.objects.get(pk=sermon_id)
			template = loader.get_template('sermon.html')
			context = {
				'sermon' : sermon
			}
		except Exception as e:
			template = loader.get_template('error.html')
			context = {
				'error' : str(e)
			}
	else:
		context = {
			'error' : '501 Invalid Request Protocol'
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))

def editsermon(request, testimonial_id):
	if request.method == 'GET':
		try:
			testimonial = Testimonial.objects.get(pk=testimonial_id)
			form = forms.Thanks()
			template = loader.get_template('thank.html')
			context = {
				'testimonial_id' : testimonial_id,
				'testimonial_title' : testimonial.testimonial_title,
				'testimonial_description' : testiomonial.testimonial_description,
				'thanks_count' : testimonial.thanks_count
			}
		except Exception:
			form = forms.Testimonial()
			context = {
				'error' : str(Exception)
			}
			template = loader.get_template('error.html')
	else:
		context = {
			'error' : '501 Invalid Request Protocol' #protocol error
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))

def removesermon(request, testimonial_id, thanks_count):
	if request.method == 'POST':
		try:
			testimonial = Testimonial.objects.get(pk=testimonial_id)
			#potentially reference other fields in prayer object to populate the rest of the form
			#increment prayer count
			count = thanks_count
			count = count + 1
			testimonial.thanks_count = count
			testimonial.save()
			return redirect('/')
		except Exception as e:
			context = {
				'error' : str(e)
			}
			template = loader.get_template('error.html')
	else:
		context = {
			'error' : '501 Invalid Request Protocol' #protocol error
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))
