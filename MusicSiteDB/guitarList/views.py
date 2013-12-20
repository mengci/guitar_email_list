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
	t = loader.get_template('templates/search.html')
	c = RequestContext(request, {
		'latest_poll_list': 1,
	})
 
	return HttpResponse(t.render(c))

@csrf_exempt
def retrieve_email(request):
	print "=" * 100
	if request.method == "POST":
		# todo: handle the saving here 
		source = request.POST.get("type")
		country = request.POST.get("country")
		state = request.POST.get("state")
		city = request.POST.get("city")
		print "*" * 100
		q = []
		if source != "" or country != "" or state != "" or city != "":
			q = Email.objects.filter(source_type__contains = source,country__contains = country,
				state__contains = state,city__contains = city)

		a = [obj.email for obj in q]

		result = {"result":a}
		print result
		x = simplejson.dumps(result)
		print "34" *20
		return HttpResponse(x, "application/json")

		print q
		
		pass
	pass