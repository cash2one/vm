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

from hashlib import md5
from datetime import *
import ImageDraw, ImageFont, random
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
#import StringIO
from PIL import Image
'''
public
@desc 用户登录
@param request 发送过来的POST请求 username password
@return 0 登录成功 user:{id,username,nickname}
        1 用户名不存在
        2 密码错误
        3 用户名或密码不能为空
        4 账户禁用
        5 验证码不能为空
        6 验证码错误
        -1 其他错误
'''
@csrf_exempt
def login_ajax(request):
    resp = {'errno': -1,'errinfo': ''}

    name = request.POST.get('username')
    pwd = request.POST.get('password')
    code = request.POST.get('checkcode')
    if (not code):
        resp = {'errno' : 5, 'errinfo' : u'验证码不能为空'}
        return HttpResponse(json.dumps(resp), mimetype = "application/json")
    if request.session["checkcode"] != code:
        resp = {'errno' : 6, 'errinfo' : u'验证码错误'}
        return HttpResponse(json.dumps(resp), mimetype = "application/json")
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


'''
生成验证码
'''
@csrf_exempt
def get_check_code_image(request):
    #图片宽度  
    width = 160  
    #图片高度  
    height = 50  
    #背景颜色  
    bgcolor = (255,255,255)  
    #生成背景图片  
    im = Image.new('RGB',(width,height),bgcolor)
    draw = ImageDraw.Draw(im)
    mp = md5()
    mp_src = mp.update(str(datetime.now()))
    mp_src = mp.hexdigest()
    rand_str = mp_src[0:4]
    draw.text((10,10), rand_str[0], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,40)), fill=(0, 0, 255))
    draw.text((48,10), rand_str[1], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,40)), fill=(0, 0, 255))
    draw.text((85,10), rand_str[2], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,40)), fill=(0, 0, 255))
    draw.text((120,10), rand_str[3], font=ImageFont.truetype("ARIAL.TTF", random.randrange(25,40)), fill=(0, 0, 255))
    request.session['checkcode'] = rand_str
    buf = StringIO.StringIO()
    try:
        im.save(buf, 'png')
    except Exception,e:
        print Exception,e
    return HttpResponse(buf.getvalue(),'image/png')

