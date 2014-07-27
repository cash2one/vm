#encoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from myuser.models import *

def index(request):
    user = request.user
    if not user.is_authenticated():
        return render_to_response('website/login.html')
    else:
        user_name = user.my_user.name
        data = {'username': user_name};
        return render_to_response('website/query_data_daily.html', data, context_instance=RequestContext(request))  

@login_required
def query_data_daily(request):
    user = request.user
    user_name = user.my_user.name
    data = {'username': user_name};
    return render_to_response('website/query_data_daily.html', data, context_instance=RequestContext(request))
    
@login_required
def query_data_hourly(request):
    user = request.user
    user_name = user.my_user.name
    print user_name
    data = {'username': user_name};
    return render_to_response('website/query_data_hourly.html', data, context_instance=RequestContext(request))
    
@login_required
def visual_data_daily(request):
    user = request.user
    user_name = user.my_user.name
    data = {'username': user_name};
    return render_to_response('website/visual_data_daily.html', data, context_instance=RequestContext(request))
    
@login_required
def visual_data_hourly(request):
    user = request.user
    user_name = user.my_user.name
    data = {'username': user_name};
    return render_to_response('website/visual_data_hourly.html', data, context_instance=RequestContext(request))
    
@login_required
def node_all(request):
    user = request.user
    user_name = user.my_user.name
    data = {'username': user_name};
    return render_to_response('website/node_all.html', data, context_instance=RequestContext(request))
    
@login_required
def node_manage(request):
    user = request.user
    user_name = user.my_user.name
    data = {'username': user_name};
    return render_to_response('website/node_manage.html', data, context_instance=RequestContext(request))