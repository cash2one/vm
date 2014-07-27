#encoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib import auth
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from myuser.models import *


'''
public
@desc 用户登录
@param request 发送过来的POST请求 username password
@return 0 登录成功 user:{id,username,nickname}
        1 用户名不存在
        2 密码错误
        3 用户名或密码不能为空
        4 账户禁用
        -1 其他错误
'''
@csrf_exempt
def login_ajax(request):
    resp = {'errno': -1,'errinfo': ''}

    name = request.POST.get('username')
    pwd = request.POST.get('password')
    if (not name) or (not pwd):
        resp = {'errno' : 3, 'errinfo' : u'用户名或密码不能为空！'}
        return HttpResponse(json.dumps(resp), mimetype = "application/json")
    user = auth.authenticate(username = name, password = pwd)
    
    if user != None:
        if user.is_active:
            auth.login(request, user)
            #token = get_token(user.password) #为实现cookie自动登录做的口令
            u = {'uid':user.id,'username':user.username,
                 'nickname':user.my_user.name}
            resp = {'errno': 0,'user':u}
            #return HttpResponseRedirect('/query_data_daily')
        else:
            resp = {'errno': -4,'errinfo': '该账户已被禁用，请联系管理员'}
    else:
        user_list = User.objects.filter(username = name)
        if (len(user_list) ==  0):
            resp = {'errno': 1,'errinfo': u'用户名不存在'}
        elif user_list[0].check_password(pwd) is False:
            resp = {'errno': 2,'errinfo': u'密码错误'}
    return HttpResponse(json.dumps(resp),mimetype="application/json")
    
'''
public
@desc 用户注销
@param request 发送过来的请求 无参数
@return 返回状态码 {'errno': 0}
'''
@csrf_exempt
def logout_ajax(request):
    resp = {'errno': 0}
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponse(json.dumps(resp),mimetype="application/json")