# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Customer,Channel,Article
from utils import serializer,auth
from django.http import HttpResponse
import json

# 获取所有用户
def get_users(request):
    customers = Customer.objects.all()
    atrs = ['id','phone','nickname','sex','icon','grade']
    json_obj = serializer.ser(customers,atrs)
    return HttpResponse(json_obj)

# 根据id获取用户
def get_user(request):
    post = request.POST
    phone = post['phone']
    customer = Customer.objects.filter(phone=phone)
    atrs = ['id','phone','nickname','sex','icon','grade']
    json_obj = serializer.ser(customer,atrs)
    return HttpResponse(json_obj)

# 获取某个用户关注的频道列表 多对多的关系 --finish
@auth
def get_user_channels(request):
    post = request.POST
    phone = post['phonenum']
    customer = Customer.objects.filter(phone = phone)
    if customer[0] == None:
        return HttpResponse('no user find !')
    channels = customer[0].channels.all()
    atrs=['id']
    json_obj = serializer.ser(channels,atrs,serflag=False)
    append ={"phonenum":customer[0].phone}
    return HttpResponse(serializer.wrap(json_obj,"userChannels",append))

# 获取某个用户关注的文章列表 多对多的关系 --finish
@auth
def get_user_articles(request):
    post = request.POST
    phone = post['phonenum']
    customer = Customer.objects.filter(phone = phone)
    if customer[0] == None:
        return HttpResponse('no user find !')
    articles = customer[0].articles.all()
    atrs = ['id','title','image','type','create_time','author','channel_id','url','desc']
    json_obj = serializer.ser(articles,atrs,serflag=False)

    return HttpResponse(serializer.wrap(json_obj,"favorites"))

# 取消关注频道
@auth
def del_user_channel(request):
    post = request.POST
    phone = post['phonenum']
    channelid = post['channelid']
    customer = Customer.objects.filter(phone = phone)
    if customer[0] == None:
        return HttpResponse('no user find !')
    channel = Channel.objects.get(id=channelid)
    customer[0].channels.remove(channel)
    return HttpResponse(json.dumps({'status':'ok'}))

# 添加关注频道
@auth
def add_user_channel(request):
    post = request.POST
    phone = post['phonenum']
    channelid = post['channelid']
    customer = Customer.objects.filter(phone = phone)
    if customer[0] == None:
        return HttpResponse('no user find !')
    channel = Channel.objects.get(id=channelid)
    customer[0].channels.add(channel)
    return HttpResponse(json.dumps({'status':'ok'}))

# 取消收藏文章
@auth
def del_user_article(request):
    post = request.POST
    phone = post['phonenum']
    articleid = post['articleid']
    customer = Customer.objects.filter(phone = phone)
    if customer[0] == None:
        return HttpResponse('no user find !')
    article = Article.objects.get(id=articleid)
    customer[0].articles.remove(article)
    return HttpResponse(json.dumps({'status':'ok'}))

# 添加收藏文章
@auth
def add_user_article(request):
    post = request.POST
    phone = post['phonenum']
    articleid = post['articleid']
    customer = Customer.objects.filter(phone = phone)
    if customer[0] == None:
        return HttpResponse('no user find !')
    article = Article.objects.get(id=articleid)
    customer[0].articles.add(article)
    return HttpResponse(json.dumps({'status':'ok'}))