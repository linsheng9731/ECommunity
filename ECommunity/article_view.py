# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Article, Channel, Collection
from utils import serializer, cors_http_response
from django.http import HttpResponse
import json
import datetime
from baiduPush import *

# 获取所有的文章
def get_articles(request):
    articles = Article.objects.all()
    atrs = ['id', 'title', 'body', 'image', 'type', 'create_time', 'author', 'channel_id', 'url', "desc"]
    json_obj = serializer.ser(articles, atrs)
    return HttpResponse(json_obj)


# 获取指定的文章 --finish
def get_article(request):
    id = request.GET["id"]
    articles = Article.objects.filter(id=id)

    ## add start
    # add by Abner
    # in order to count the read times of specific article
    if (len(articles) != 0):
        articles[0].read_times += 1
        articles[0].save()

    ## add end

    atrs = ['id', 'title', 'body', 'image', 'type', 'create_time', 'author', 'channel_id', 'url', "desc"]
    json_obj = serializer.ser(articles, atrs, serflag=False)

    final_obj_json = json.dumps(json_obj[0])
    result = jsonpHelper(request, final_obj_json)

    return HttpResponse(result, content_type="application/json")


def get_channel_articles(request):
    get = request.GET
    id = get['channelid']
    day = get['date']
    channel = Channel.objects.get(id=id)
    if day == u'0':
        day = "9999-9-99"
    else:
        day = unicode(day)
    articles_obj, collection_obj, create_time, create_time_old = merge_articles_collections(channel, day,
                                                                                            id)
    for obj in articles_obj:
        collection_obj.append(obj)
    datatmp = {"date": create_time, "pre_date": create_time_old}
    return HttpResponse(serializer.wrap(collection_obj, "articles", datatmp))


# 推送提醒
def push_news(request):
    post = request.POST
    title = post['title']
    desc = post['desc']
    msgtitle = {'title': title, "description": desc}
    msgtitle = json.dumps(msgtitle)
    ret = pushMessageAll(msgtitle, 1)
    print(ret)
    return HttpResponse("推送成功！")


# 根据id推送文章
def push_article(request):
    post = request.POST
    id = post["id"]
    objects = Article.objects.filter(id=id)
    atrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', "desc"]  # 降序
    articles_obj = serializer.ser(objects, atrs, serflag=False)  # 不进行序列化
    datatmp = {"date": '0', "pre_date": '0'}
    msg = serializer.wrap(articles_obj, "articles", datatmp)
    ret = pushMessageAll(msg, 0)
    print(ret)

    return cors_http_response("OK")


def max2(args):
    list = []
    for obj in args:
        list.append(obj)
    sets = set(list)
    sorted_sets = sorted(sets, reverse=True)
    return sorted_sets


# 根据channel 时间 来筛选出文章和集合
def merge_articles_collections(channel, day, id):
    create_times = []
    raw = "select DISTINCT create_time,id from ECommunity_article where create_time<=" + "'" + unicode(
        day) + "'" + " and channel_id=" + unicode(id) + " GROUP by create_time order by create_time DESC limit 2"
    raw_query_set = Article.objects.raw(raw)
    for item in raw_query_set:
        create_times.append(item.create_time)
    raw = "select DISTINCT create_time,id from ECommunity_collection where create_time<=" + "'" + unicode(
        day) + "'" + " and channel_id=" + unicode(id) + " GROUP by create_time order by create_time DESC limit 2"
    raw_query_set = Collection.objects.raw(raw)
    for item in raw_query_set:
        create_times.append(item.create_time)
    max2date = max2(create_times)
    if len(max2date) >= 2:
        create_time = max2date[0]
        create_time_old = max2date[1]
    else:
        create_time_old = u'0'
        create_time = u'0'
        if len(create_times) >= 1:
            create_time = max2date[0]
    articles = Article.objects.filter(create_time=create_time, channel=channel).order_by("-id")
    collections = Collection.objects.filter(create_time=create_time, channel=channel).order_by("-id")
    atrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', "desc"]  # 降序
    articles_obj = serializer.ser(articles, atrs, serflag=False)  # 不进行序列化
    atrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', "desc"]  # 降序
    collection_obj = serializer.ser(collections, atrs, serflag=False)  # 不进行序列化
    return articles_obj, collection_obj, create_time, create_time_old


# 根据时间筛选单天的文章和合集
def merge_articles_collections_all(day):
    create_times = []
    raw = "select DISTINCT create_time,id from ECommunity_article where create_time<=" + "'" + unicode(
        day) + "'" + " GROUP by create_time order by create_time DESC limit 2"
    raw_query_set = Article.objects.raw(raw)
    for item in raw_query_set:
        create_times.append(item.create_time)
    raw = "select DISTINCT create_time,id from ECommunity_collection where create_time<=" + "'" + unicode(
        day) + "'" + " GROUP by create_time order by create_time DESC limit 2"
    raw_query_set = Collection.objects.raw(raw)
    for item in raw_query_set:
        create_times.append(item.create_time)
    max2date = max2(create_times)
    if len(max2date) >= 2:
        create_time = max2date[0]
        create_time_old = max2date[1]
    else:
        create_time_old = u'0'
        create_time = u'0'
        if len(create_times) >= 1:
            create_time = max2date[0]
    articles = Article.objects.filter(create_time=create_time)
    collections = Collection.objects.filter(create_time=create_time)
    atrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', "desc"]  # 降序
    articles_obj = serializer.ser(articles, atrs, serflag=False)  # 不进行序列化
    atrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', "desc"]  # 降序
    collection_obj = serializer.ser(collections, atrs, serflag=False)  # 不进行序列化
    return articles_obj, collection_obj, create_time, create_time_old


def jsonpHelper(request, data):
    if 'callback' in request.GET:
        data = '%s(%s);' % (request.GET['callback'], data)
    return data


def getHotArticles(request):
    articles = Article.objects.order_by("-read_times")[0:6]

    atrs = ['id', 'title', 'image', 'url', "desc"]
    json_obj = serializer.ser(articles, atrs, serflag=False)
    json_obj = json.dumps(json_obj)
    json_obj = jsonpHelper(request, json_obj)

    return HttpResponse(json_obj, content_type="application/json")
