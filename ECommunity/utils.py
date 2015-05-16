# coding:utf8 #
__author__ = 'damon_lin'

import json

class serializer():

    atrs=[]

    @classmethod
    def ser(self,model,param):
        json_obj = []
        self.atrs = param
        for item in model:
            obj = {}
            for atr in self.atrs:
                obj[atr] = getattr(item,atr)
            json_obj.append(obj)
        return json.dumps(json_obj)

    @classmethod
    def cov(self,item):
        if item == None:
            item = 'None'
        return (item).encode('utf-8')