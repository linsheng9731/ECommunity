# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Article, Collection, Channel
from utils import serializer
from django.http import HttpResponse
import json


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
    json_obj = serializer.ser(articles, attrs,serflag=False)

    return HttpResponse(serializer.wrap(json_obj,"collects"))


# add Collection
# def add_Collection(request):
# post = request.POST
# phone = post['phonenum']
# Collection = Collection()
#     Collection.save()
#     return HttpResponse(json.dumps({'status':'ok'}))

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
