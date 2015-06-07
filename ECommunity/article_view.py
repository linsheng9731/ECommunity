# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Article, Channel, Collection
from utils import serializer
from django.http import HttpResponse
import json
import datetime

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
    atrs = ['id', 'title', 'body', 'image', 'type', 'create_time', 'author', 'channel_id', 'url', "desc"]
    json_obj = serializer.ser(articles, atrs, serflag=False)
    final_obj = json_obj[0]
    return HttpResponse(json.dumps(final_obj))


# 根据频道id来筛选文章,需要分页,插入时需要考虑day属性 --finish
def get_channel_articles(request):
    get = request.GET
    id = get['channelid']
    day = get['date']
    channel = Channel.objects.get(id=id)
    create_times = []
    if day == u'0':
        day = "9999-9-99"
    else:
        day = unicode(day)
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
        if len(create_times)>=1:
            create_time = max2date[0]

    articles = Article.objects.filter(create_time=create_time, channel=channel)
    collections = Collection.objects.filter(create_time=create_time, channel=channel)

    atrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', "desc"]  # 降序
    articles_obj = serializer.ser(articles, atrs, serflag=False)  # 不进行序列化
    atrs = ['id', 'title', 'image', 'type', 'create_time', 'author', 'channel_id', "desc"]  # 降序
    collection_obj = serializer.ser(collections, atrs, serflag=False)  # 不进行序列化
    for obj in articles_obj:
        collection_obj.append(obj)
    datatmp = {"date": create_time, "pre_date": create_time_old}

    return HttpResponse(serializer.wrap(collection_obj, "articles", datatmp))


def max2(args):
    list = []
    for obj in args:
        list.append(obj)
    sets = set(list)
    sorted_sets = sorted(sets, reverse=True)
    return sorted_sets

