# coding:utf8 #
__author__ = 'damon_lin'

import json

class serializer():

    atrs=[]


    @classmethod
    def ser(self,model,param,serflag=True):  # model:待序列化的模型 param:待序列化的参数
        json_obj = []
        self.atrs = param
        for item in model:   # 将特殊对象转化成普通map对象
            obj = {}
            for atr in self.atrs:
                obj[atr] = getattr(item,atr)
            json_obj.append(obj)  # 将普通map对象转化成json格式
        if serflag:
            return json.dumps(json_obj)
        else:
            return json_obj

    @classmethod
    def cov(self,item):
        if item == None:
            item = 'None'
        return (item).encode('utf-8')