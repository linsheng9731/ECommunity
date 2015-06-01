#coding=utf8
__author__ = 'abnerzheng'

from models import Article, Channel
from haystack.query import SearchQuerySet
from django.http import HttpResponse
import json


def getSearchResult(request):
    if 'q' not in request.GET:
        return HttpResponse(json.dumps({'state':'fail'}))

    searchKey = request.GET['q']
    result = SearchQuerySet().filter(content=searchKey)
    if len(result)==0:
        return HttpResponse(json.dumps({'search':[]}))
    return HttpResponse(convertToFormat(result))


def convertToFormat(items):
    params = ['id', 'channel_id', 'type', 'title',
              'create_time', 'image', 'desc', 'url']
    articles = []
    channels = []
    for e in items:
        if isinstance(e.object, Article):
            articles.append(e.object)
        else:
            channels.append(e.object)

    tmp = []
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
            aa[attr] = getattr(e, attr) if attr != 'type' else "1"
        tmp.append(aa)

    tmp.append({"id": "0",
                "channel_id": "0",
                "type": "0",
                "title": u'文章',
                "create_time": "0",
                "image": "",
                "desc": "",
                "url": ""})

    for e in articles:
        aa = {}
        for attr in params:
            aa[attr] = getattr(e, attr) if attr != 'type' else "2"
        tmp.append(aa)

    return json.dumps({'search':tmp})

