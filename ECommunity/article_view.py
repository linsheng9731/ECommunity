# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Article,Channel
from utils import serializer
from django.http import HttpResponse

#获取所有的文章
def get_articles(request):
    articles = Article.objects.all()
    atrs = ['id','title','body','img','type','create_time','author','channel_id','url']
    json_obj = serializer.ser(articles,atrs)
    return HttpResponse(json_obj)

#根据频道id来筛选文章
def get_channel_articles(request):
    post = request.POST
    id = post['id']
    channel = Channel.objects.get(id=id)
    articles = Article.objects.filter(channel=channel)
    atrs = ['id','title','body','img','type','create_time','author','channel_id','url']
    json_obj = serializer.ser(articles,atrs)
    return HttpResponse(json_obj)