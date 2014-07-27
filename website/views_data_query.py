
#encoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from myuser.models import *
from website.models import *

def search_daily(request):
    resp = {'errno': -1,'errinfo': ''}
    monitor_type = request.GET.get('monitor_type')
    search_type = request.GET.get('search_type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    data_status = request.GET.get('data_status')
    node_id = request.GET.get('node_id')
    # step 0. 数据处理
    start_date_vec = start_date.split('/')
    start_year = int(start_date_vec[0])
    start_month = int(start_date_vec[1])
    start_day = int(start_date_vec[2])
    end_date_vec = end_date.split('/')
    end_year = int(end_date_vec[0])
    end_month = int(end_date_vec[1])
    end_day = int(end_date_vec[2])
    # step 1. 采集器
    if monitor_type == 'c':
        # 1.1. 电压
        if search_type == 'voltage':
            # 1.1.1. 数据状态 -- 全部
            if data_status == 'all':
                CDailyData.objects.filter(node__name_id=node_id, data_time__gte=datetime.date(start_year, start_month, start_day), date_time__lte=datetime.date(end_year, end_month, end_day)).values('max_voltage', 'min_voltage', 'avg_voltage', 'mse_voltage', 'voltage_failure_times', 'voltage_exception_times', 'voltage_exception_period', )
    # step 2. 恒电位仪
    elif monitor_type == 'h':
        pass
