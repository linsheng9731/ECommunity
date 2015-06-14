# coding:utf8 #
__author__ = 'damon_lin'

import json
from  lib import *
from django.contrib.auth import *
from django.contrib.auth.views import *
from django.contrib.auth.models import User

# 序列化对象
class serializer():
    atrs = []
    @classmethod
    def ser(self, model, param, serflag=True):  # model:待序列化的模型 param:待序列化的参数
        json_obj = []
        self.atrs = param
        for item in model:  # 将特殊对象转化成普通map对象
            obj = {}
            for atr in self.atrs:
                obj[atr] = getattr(item, atr)
            json_obj.append(obj)  # 将普通map对象转化成json格式
        if serflag:
            return json.dumps(json_obj)  # 转化为json对象
        else:
            return json_obj

    @classmethod
    def wrap(self, json_obj, objname=None, append=None):
        final_obj = {}
        if append:
            for k, v in append.items():
                final_obj[k] = v
        final_obj[objname] = json_obj
        json_obj = json.dumps(final_obj)
        return json_obj

    @classmethod
    def cov(self, item):
        if item == None:
            item = 'None'
        return (item).encode('utf-8')

# 验证装饰
def auth(func):
    def _deco(request):
        try:
            if len(request.POST)>0:
              dic = request.POST
            else:
              dic = request.GET
            name = dic["phonenum"]
            pws = dic["pwd"]
            request.session["dic"] = dic
            user = authenticate(username=name, password=pws)
            if user is not None:
                auth_login(request, user)
            else:
                print "user is None"
                return HttpResponse(json.dumps({'state': 'FAILED'}))
        except Exception,e:
            print "Exception occured"
            print e
            return HttpResponse(json.dumps({'state': 'FAILED'}))
        ret = func(request)
        return ret
    return _deco



