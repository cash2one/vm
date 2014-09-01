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

@csrf_exempt
def search_daily(request):
    # step 0. 数据接收
    resp = {'error':1}
    monitor_type = request.POST['monitor_type']
    search_type = request.POST['search_type']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    data_status = request.POST['data_status']
    node_id = request.POST['node_list']
    # step 1. 采集器
    if monitor_type == 'c':
        # 1.1. 电压
        if search_type == 'voltage':
            # 1.1.1. 数据状态 -- 全部
            if data_status == 'all':
                infos = CDailyData.objects.filter(node__name_id=int(node_id), data_time__gte=start_date, data_time__lte=end_date).values_list('data_time','node__name_id','max_voltage', 'min_voltage', 'avg_voltage', 'mse_voltage', 'voltage_failure_times', 'voltage_exception_times', 'voltage_exception_period')
                _compose_resp(infos, resp)
            # 1.1.2. 数据状态 -- 正常
            elif data_status == 'normal':
                infos = CDailyData.objects.filter(node__name_id=int(node_id), data_time__gte=start_date, data_time__lte=end_date, voltage_failure_times=0, voltage_exception_times=0).values_list('data_time','node__name_id','max_voltage', 'min_voltage', 'avg_voltage', 'mse_voltage', 'voltage_failure_times', 'voltage_exception_times', 'voltage_exception_period')
                _compose_resp(infos, resp)
            # 1.1.3. 数据状态 -- 异常
            elif data_status == 'except':
                infos = CDailyData.objects.filter(node__name_id=int(node_id), data_time__gte=start_date, data_time__lte=end_date, voltage_failure_times__gt=0, voltage_exception_times__gt=0).values_list('data_time','node__name_id','max_voltage', 'min_voltage', 'avg_voltage', 'mse_voltage', 'voltage_failure_times', 'voltage_exception_times', 'voltage_exception_period')
                _compose_resp(infos, resp)
                
    ## step 2. 恒电位仪
    #elif monitor_type == 'h':
    #    pass
    return HttpResponse(json.dumps(resp),content_type="application/json")

def _compose_resp(infos, resp):
    resp['error'] = 0
    resp['result'] = []
    for info in infos:
        info_list = list(info)
        info_list[0] = str(info_list[0])
        resp['result'].append(info_list)