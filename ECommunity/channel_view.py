# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Channel
from django.http import HttpResponse
from utils import serializer
import json

#获取所有的频道列表
def get_channels(request):
    channels = Channel.objects.all()
    atrs=['id','img','cata','num','title','dec','type']
    json_obj = serializer.ser(channels,atrs)
    return HttpResponse(json_obj)