# coding:utf-8 #
__author__ = 'damon_lin'

from lib import *
from models import Comment, Customer, Article
from utils import serializer


def get_user_comments(request):
    post = request.POST
    user_id = post["user_id"]
    comments = Comment.objects.filter(customer=user_id)
    attrs = ["content"]
    json_obj = serializer.ser(comments, attrs)
    return HttpResponse(json_obj)

def get_article_comments(request):
    post = request.POST
    article_id = post["article_id"]
    comments = Comment.objects.filter(article=article_id)
    attrs = ["content"]
    json_obj = serializer.ser(comments, attrs)
    return HttpResponse(json_obj)


# must check if user had added comment !
def add_comment(request):
    post = request.POST
    article_id = post["article_id"]
    user_id = post["user_id"]
    customers = Customer.objects.filter(id=user_id)
    if len(customers) <=0:
        return HttpResponse(json.dumps({"status": "FAILED user doesn't exist"}))
    customer = customers[0]
    articles = Article.objects.filter(id=article_id)
    if len(articles) <=0:
        return HttpResponse(json.dumps({"status": "FAILED article doesn't exist"}))
    article = articles[0]
    content = post["content"]
    comments = Comment.objects.filter(customer=customer, article=article, content=content)
    if len(comments) > 0:
        return HttpResponse(json.dumps({"status": "FAILED"}))
    comment = Comment(customer=customer, article=article,content=content)
    comment.save()
    return HttpResponse(json.dumps({"status": "OK"}))