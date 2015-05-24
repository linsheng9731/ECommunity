# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Customer,Channel
from utils import serializer
from django.http import HttpResponse

#获取所有用户
def get_users(request):
    customers = Customer.objects.all()
    atrs = ['id','phone','nickname','sex','icon','grade']
    json_obj = serializer.ser(customers,atrs)
    return HttpResponse(json_obj)

#根据id获取用户
def get_user(request):
    post = request.POST
    phone = post['phone']
    customer = Customer.objects.filter(phone=phone)
    atrs = ['id','phone','nickname','sex','icon','grade']
    json_obj = serializer.ser(customer,atrs)
    return HttpResponse(json_obj)

#获取某个用户关注的频道列表 多对多的关系
def get_user_channels(request):
    post = request.POST
    id = post['id']
    customer = Customer.objects.filter(id = id)
    if customer[0] == None:
        return HttpResponse('no user find !')
    channels = customer[0].channels.all()
    atrs=['id','img','cata','num','title','desc','type']
    json_obj = serializer.ser(channels,atrs)
    return HttpResponse(json_obj)

#获取某个用户关注的文章列表 多对多的关系
def get_user_articles(request):
    post = request.POST
    id = post['id']
    customer = Customer.objects.filter(id = id)
    if customer[0] == None:
        return HttpResponse('no user find !')
    articles = customer[0].articles.all()
    atrs = ['id','title','body','img','type','create_time','author','channel_id','url']
    json_obj = serializer.ser(articles,atrs)

    return HttpResponse(json_obj)

