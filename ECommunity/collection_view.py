# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import articles,Collection,
from utils import serializer
from django.http import HttpResponse
import json

                    
 
def add_Collection_articles(request):
    post = request.POST
    id = post['id']
    articlesid=post['articlesid']
    pwd = post['pwd'] # 验证预留
    Collections = Collection.objects.filter(id = id)
    if Collections[0] == None:
        return HttpResponse('not find !')
    articles = articles.objects.get(id=articlesid)
    Collections[0].articless.add(articles)
    return HttpResponse(json.dumps({'status':'ok'}))


def del_Collection_articles(request):
    post = request.POST
    id = post['id']
    articlesid=post['articlesid']
    pwd = post['pwd'] # 验证预留
    Collections = Collection.objects.filter(id = id)
    if Collections[0] == None:
        return HttpResponse('not find !')
    articles = articles.objects.get(id=articlesid)
    Collections[0].articless.remove(articles)
    return HttpResponse(json.dumps({'status':'ok'}))

# get Collection articles
def get_Collection_articless(request):
	post = request.POST
	id = post['id']
    articless = articles.objects.filter(id=id)
    articles = articless[0]
	atrs=[]
    atrs.append('id')
    atrs.append('title')
    	json_obj = serializer.ser(articles,atrs)
	return HttpResponse(json_obj)



        
 
# add Collection
def add_Collection(request):
    post = request.POST
    phone = post['phonenum']

   Collection = Collection()
   Collection.save()
   
    return HttpResponse(json.dumps({'status':'ok'}))

# delete Collection
def del_Collection(request):
    post = request.POST
    id = post['id']
    Collections = Collection.objects.filter(id = id)
    if Collections[0] == None:
    	return HttpResponse('not find !')
    Collections[0].delete()
    return HttpResponse(json.dumps({'status':'ok'}))

def update_Collection(request):
    post = request.POST
    phone = post['phonenum']
    id = post['id']
    Collections = Collection.objects.filter(id=id)
    Collection = Collections[0]
    # update
    Collection = Collection()
    Collection.save()

    return HttpResponse(json.dumps({'status':'ok'}))


# get Collection
def get_Collection(request):
    post = request.POST
    id = post['id']
    Collections = Collection.objects.filter(id=id)
    Collection = Collections[0]
    atrs=[]
    atrs.append('title')
    atrs.append('image')
    atrs.append('desc')
    atrs.append('create_time')
        json_obj = serializer.ser(Collection,atrs)
    return HttpResponse(json_obj)

    
