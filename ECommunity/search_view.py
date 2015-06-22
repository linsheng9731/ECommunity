#coding=utf8
__author__ = 'abnerzheng'

from models import Article, Channel, Search, Collection
from haystack.query import SearchQuerySet
from django.http import HttpResponse
import json
import jieba.analyse


def getHotkey(request):
    num = request.GET.get("num",20)
    hotKeyWordsObjs = Search.objects.order_by("freq")[0:num]
    hotkeys = [e.keyword for e in hotKeyWordsObjs]
    return HttpResponse(json.dumps(hotkeys))



def getSearchResult(request):
    if 'q' not in request.GET:
        return HttpResponse(json.dumps({'state':'fail'}))

    searchKey = request.GET['q']
    #统计词频
    if len(searchKey):
        ext_tags = jieba.analyse.extract_tags(searchKey,6)
        for e in ext_tags:
            if len(e)>1:
                a = Search.objects.filter(keyword=e)
                if(len(a)):
                    a[0].freq += 1
                    a[0].save()
                else:
                    Search(keyword=e,freq=1).save()


    result = SearchQuerySet().filter(content=searchKey)[0:50]
    if len(result)==0:
        return HttpResponse(json.dumps({'search':[]}))
    return HttpResponse(convertToFormat(result,searchKey))


def convertToFormat(items,searchKey):
    params = ['id', 'type', 'title',
               'image', 'desc']
    articles = []
    channels = []
    collection = []
    for e in items:
        if isinstance(e.object, Article):
            articles.append(e.object)
        elif isinstance(e.object, Collection):
            collection.append(e.object)
        elif e.object.type == '1':
            channels.append(e.object)

    tmp = []
    if(len(channels)>0):
        tmp.append({"id": "0",
                "channel_id": "0",
                "type": "0",
                "title": u"频道",
                "create_time": "0",
                "image": "",
                "desc": "",
                "url": ""})
    for e in channels:
        aa = {}
        for attr in params:
            if attr == "id":
                aa["channel_id"] = getattr(e,attr)
                continue
            aa[attr] = getattr(e, attr) if attr != 'type' else "1"
        tmp.append(aa)

    if(len(collection)>0):
        tmp.append({"id": "0",
                "channel_id": "0",
                "type": "0",
                "title": u"合辑",
                "create_time": "0",
                "image": "",
                "desc": "",
                "url": ""})

    params.append("channel_id")
    params.append("create_time")
    for e in collection:
        aa = {}
        for attr in params:
            aa[attr] = getattr(e, attr) if attr != 'type' else "3"
        tmp.append(aa)

    if(len(articles)>0):
        tmp.append({"id": "0",
                "channel_id": "0",
                "type": "0",
                "title": u'文章',
                "create_time": "0",
                "image": "",
                "desc": "",
                "url": ""})

    params.append("url")
    for e in articles:
        aa = {}

        for attr in params:
            aa[attr] = getattr(e, attr) if attr != 'type' else "2"
        tmp.append(aa)

    return json.dumps({'search':tmp, "key":searchKey})

