# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import Article,Channel
from utils import serializer
from django.http import HttpResponse
import json
import datetime

# 获取所有的文章
def get_articles(request):
    articles = Article.objects.all()
    atrs = ['id','title','body','image','type','create_time','author','channel_id','url',"desc"]
    json_obj = serializer.ser(articles,atrs)
    return HttpResponse(json_obj)

# 获取指定的文章 --finish
def get_article(request):
    id = request.GET["id"]
    articles = Article.objects.filter(id = id)
    atrs = ['id','title','body','image','type','create_time','author','channel_id','url',"desc"]
    json_obj = serializer.ser(articles,atrs,serflag=False)
    final_obj = json_obj[0]
    return HttpResponse(json.dumps(final_obj))

# 根据频道id来筛选文章,需要分页,插入时需要考虑day属性 --finish
def get_channel_articles(request):
    get = request.GET
    id = get['channelid']
    day = get['date']
    channel = Channel.objects.get(id=id)

    # create_time = datetime.datetime.now()-datetime.timedelta(days=1)
    articles = Article.objects.filter(channel=channel).order_by('-day')  # 获取最大更新次数
    max_day = articles[0].day
    day = int(max_day) - int(day)  # 获取当前查询更新次数
    articles = Article.objects.filter(channel=channel,day=str(day)).order_by('-create_time')  # 降序

    atrs = ['id','title','image','type','create_time','author','channel_id','url',"desc"]  # 降序
    json_obj = serializer.ser(articles,atrs,serflag=False)  # 不进行序列化
    datatmp = {"date":"123"}
    return HttpResponse(serializer.wrap(json_obj,"articles",datatmp))