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
from django.template.loader import get_template
from django.template import Context
from website.utils import getNodeIdList, getNetNameList

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
'''    
@login_required
def node_all(request):
    user = request.user
    user_name = user.my_user.name
    data = {'username': user_name};
    return render_to_response('website/node_all.html', data, context_instance=RequestContext(request))
'''  

@login_required
def node_all(request):
    user = request.user
    if not user.is_authenticated():
        return render_to_response('website/login.html')
    user_name = user.my_user.name
    net_list = getNetNameList(user.my_user)
    node_list = getNodeIdList(user.my_user)
    t = get_template('website/node_all.html')
    html = t.render(Context({'net_list': net_list, 'node_list': node_list, 'username':user_name}))
    return HttpResponse(html)

    
@login_required
def node_manage(request):
    user = request.user
    user_name = user.my_user.name
    data = {'username': user_name};
    return render_to_response('website/node_manage.html', data, context_instance=RequestContext(request))