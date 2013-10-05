from django import forms
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from guitarList.models import Email
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
import datetime, random, sha
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone

import json as simplejson

def index(request):
	t = loader.get_template('templates/save.html')
	c = RequestContext(request, {
		'latest_poll_list': 1,
	})

	return HttpResponse(t.render(c))

@csrf_exempt
def save_email(request):
	print "=" * 100
	if request.method == "POST":
		# todo: handle the saving here 
		name = request.POST.get("name")
		email = request.POST.get("email")
		source = request.POST.get("source")
		country = request.POST.get("country")
		state = request.POST.get("state")
		city = request.POST.get("city")

		Email.objects.all()
		e = Email(name=name, email=email, source_type=source, country=country, 
			state=state,city=city,created_date=timezone.now())
		e.save()

		result = {"name":name}
		x = simplejson.dumps(result)
		return HttpResponse(x, "application/json")

		print e.email_id
		
		pass
	pass