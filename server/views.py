from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .spider import spider_main
import json
import urllib.parse as urlparse


# Create your views here.

def getGuitarSheet(request):
    data = {}
    if request.body:
        bodyStr = str(request.body, 'utf-8')
        jsonStr = urlparse.unquote(bodyStr)
        print("\n request.body:", jsonStr, "-", type(request))
        data = json.loads(jsonStr.split('=')[1].replace('+', ' '))
        print('data:', data)
    else:
        data['macAddress'] = 'aa.bb.cc.dd'
        data['rootUrl'] = 'http://www.17jita.com'
        data['urlTag'] = 'base'
        data['pageTitle'] = '吉他谱'
        data['pageClass'] = 'pg'
        data['objClass'] = 'xi2'
        data['objTagClass'] = 'bm_c xld'
        data['filter'] = ''



    # return None
    spider = spider_main.SpiderMain()

    jsonDict = spider.craw(data)

    dataJson = json.dumps(jsonDict)
    print(dataJson)
    if request.method == 'GET':
        resp = HttpResponse(dataJson, content_type="application/json")
        return resp
    else:
        resp = HttpResponse(dataJson, content_type="application/json")
        return resp
