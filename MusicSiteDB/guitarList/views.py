from django import forms
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from guitarList.models import Email
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, loader
import datetime, random, sha

def index(request):
	t = loader.get_template('templates/save.html')
	c = RequestContext(request, {
		'latest_poll_list': 1,
	})

	return HttpResponse(t.render(c))

def save(request):
	pass