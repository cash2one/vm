from django.shortcuts import render
from django.http import HttpResponse
import json
import time
import datetime
# Create your views here.
def getDataHourly(request):
    if request.is_ajax():
        temp = datetime.datetime.now().second
        #temp = time.time()
        i = 0
        data = [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
        dataVector = []
        for val in data:
            temp = temp + 1
            dataVector.append([temp, val])
        jsonData = json.dumps(dataVector, ensure_ascii=False)
        return HttpResponse(jsonData, content_type="application/json")