# coding:utf8 #
from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ECommunity.models import News
from News.serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Json response wrapped from HttpResponse #
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
@api_view(['GET', 'POST'])
def list_news(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        #tmp = JSONResponse(serializer.data)
        #return JSONResponse(serializer.data)

        return Response(serializer.data)
    elif request.method == 'POST':
        return HttpResponse('post method')

