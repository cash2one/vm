#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from website.models import Node
import json
import time
import datetime
from django.template.loader import get_template
from django.template import Context
from website.utils import getNodeIdList, getNetNameList
# Create your views here.
@csrf_exempt
def getDataHourly(request):
    if request.is_ajax():
        start_date = request.POST['start_date']
        data_type = request.POST['data_type']
        node_name_id = int(request.POST['node_id'])
        
        t = time.strptime(start_date, "%Y/%m/%d")
        d = datetime.datetime(*t[:6])
        print d
        d1 = d + datetime.timedelta(days=1)
        print d1
        node = Node.objects.get(name_id=1)
        
        #node_name_id = Node.objects.all()
        #cminutedata_list = CMinuteData.objects.filter(node=node.id).order_by(data_time)
        #cminutedata_list = CMinuteData.objects.filter(node=7).order_by(data_time)
        #cminutedata_list = node.cminutedata_set.all().order_by('data_time')
        cminutedata_list = node.cminutedata_set.all().filter(data_time__gte=d, data_time__lt=d1)
        data_vector = []
        for cminutedata in cminutedata_list:
            v = cminutedata.potential
            data_time = cminutedata.data_time
            #time_str = data_time.strftime("%M:%S")
            timeStamp = int(time.mktime(data_time.timetuple()) * 1000)
            #timeStamp = int(time.mktime(data_time.timetuple())) * 1000
            print timeStamp
            #timeStamp = 1406358888074
            data_vector.append([timeStamp, v])
            timeStamp += 1000
        
        
        
        
        '''#temp = datetime.datetime.now().second
        #temp = time.time() * 1000
        #temp = int(round(time.time() * 1000))
        temp = int(time.time() * 1000)
        #temp = 1406358888074
        #temp = time.time()
        i = 0
        data = [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
        dataVector = []
        timeVector = []
        for val in data:
            #time_str = time.strftime("%M:%S", time.localtime(temp))
            #dataVector.append([time_str, val])
            #timeVector.append(time_str)
            dataVector.append([temp, val])
            temp = temp + 1000
        #dataMap = {"time" : timeVector, "data" : dataVector}
        #jsonData = json.dumps(dataMap, ensure_ascii=False)'''
        
        
        jsonData = json.dumps(data_vector, ensure_ascii=False)
        return HttpResponse(jsonData, content_type="application/json")
    
@csrf_exempt
def getNodeDesc(request):
    return HttpResponse("五道口")

@csrf_exempt
def node_all(request):
    user = request.user
    if not user.is_authenticated():
        return render_to_response('website/login.html')
    user_name = user.my_user.name
    #data = {'username': user_name};
    #net_list = Node.objects.values('net_name')
    net_list = getNetNameList(user.my_user)
    print net_list
    #node_list = Node.objects.values('name_id')
    node_list = getNodeIdList(user.my_user)
    print node_list
    node_id = None
    if 'node_id' in request.GET:
        node_id = request.GET['node_id']
        #print 'node_id ', node_id
    t = get_template('website/node_all.html')
    if node_id is not None:
        node = Node.objects.get(name_id=node_id)
        company_name = node.company.name
        net_name = node.net_name
        alias = node.alias
        desc = node.desc
        max_voltage = node.max_voltage
        min_voltage = node.min_voltage
        max_current = node.max_current
        min_current = node.min_current
        latitude = node.latitude
        longitude = node.longitude
        sim_id = node.sim_id
        expire_time = node.expire_time
        create_time = node.create_time
        info = {'company_name':company_name, 'net_name':net_name, 'node_id':node_id, 'alias':alias, 'desc':desc,
                'max_voltage':max_voltage, 'min_voltage':min_voltage, 'max_current':max_current, 'min_current':min_current,
                'latitude':latitude, 'longitude':longitude, 'sim_id':sim_id, 'expire_time':expire_time, 'create_time':create_time}
        html = t.render(Context({'net_list': net_list, 'node_list': node_list,
                                 'node_id': node_id, 'info':info, 'username':user_name}))
    else:
        html = t.render(Context({'net_list': net_list, 'node_list': node_list, 'username':user_name}))
    print 'node_id', node_id
    return HttpResponse(html)