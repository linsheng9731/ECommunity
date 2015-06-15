# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Article, Collection, Channel
from utils import serializer
from django.http import HttpResponse
import json
from lib import *
from utils import auth


def add_collection_articles(request):
    post = request.POST
    id = post['id']
    Articlesid = post['Articlesid']
    pwd = post['pwd']  # 验证预留
    Collections = Collection.objects.filter(id=id)
    if Collections[0] == None:
        return HttpResponse('not find !')
    Articles = Article.objects.get(id=Articlesid)
    Collections[0].Articless.add(Articles)
    return HttpResponse(json.dumps({'status': 'ok'}))


def del_collection_articles(request):
    post = request.POST
    id = post['id']
    Articlesid = post['Articlesid']
    pwd = post['pwd']  # 验证预留
    Collections = Collection.objects.filter(id=id)
    if Collections[0] == None:
        return HttpResponse('not find !')
    Articles = Article.objects.get(id=Articlesid)
    Collections[0].Articless.remove(Articles)
    return HttpResponse(json.dumps({'status': 'ok'}))


# get Collection Articles
def get_collection_articles(request):
    get = request.GET
    id = get['id']
    collections = Collection.objects.filter(id=id).order_by("-create_time")
    collection = collections[0]
    articles = collection.articles.all().order_by("-create_time");
    attrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', 'url', "desc"]
    json_obj = serializer.ser(articles, attrs, serflag=False)

    return HttpResponse(serializer.wrap(json_obj, "collects"))


# add Collection
# def add_Collection(request):
# post = request.POST
# phone = post['phonenum']
# Collection = Collection()
# Collection.save()
# return HttpResponse(json.dumps({'status':'ok'}))

# delete Collection
def del_collection(request):
    post = request.POST
    id = post['id']
    Collections = Collection.objects.filter(id=id)
    if Collections[0] == None:
        return HttpResponse('not find !')
    Collections[0].delete()
    return HttpResponse(json.dumps({'status': 'ok'}))


# def update_Collection(request):
#     post = request.POST
#     phone = post['phonenum']
#     id = post['id']
#     Collections = Collection.objects.filter(id=id)
#     collection = Collections[0]
#     # update
#     Collection = Collection()
#     Collection.save()
#
#     return HttpResponse(json.dumps({'status': 'ok'}))


# get Collection
def get_collections(request):
    get = request.GET
    channel_id = get['channelid']
    day = get['date']
    channel = Channel.objects.get(id=id)

    collections = Collection.objects.filter(channel=channel_id).order_by('-create_time')  # 降序

    atrs = ['id', 'title', 'image', 'create_time', "desc"]
    json_obj = serializer.ser(collections, atrs, serflag=False)  # 不进行序列化
    datatmp = {"date": "123"}
    return HttpResponse(serializer.wrap(json_obj, "articles", datatmp))


# get classes means get collections from channels
@auth
def get_user_lessons(request):
    user = request.user
    customers = Customer.objects.filter(user=user)
    customer = customers[0]
    channels = customer.channels.all()
    channels_id = []
    for item in channels:
        channels_id.append(item.id)
    collections = Collection.objects.filter().order_by('-create_time')  # 降序
    results = []
    for item in collections:
        if channels_id.__contains__(item.channel.id):
            results.append(item)
    atrs = ['id', 'title', 'image', 'create_time', "desc", "channel_id"]
    json_obj = serializer.ser(results, atrs, serflag=False)  # 不进行序列化
    datatmp = {"date": "123"}
    return HttpResponse(serializer.wrap(json_obj, "articles", datatmp))
