# coding:utf-8 #
__author__ = 'damon_lin'

from lib import *
from models import Comment, Customer, Article
from utils import serializer

# get a customer's comment for a specific article
@auth
def get_user_comments(request):
    dic = request.session["dic"]
    article_id = dic["article_id"]
    user = request.user
    customers = Customer.objects.filter(user=user)
    customer = customers[0]
    comments = Comment.objects.filter(customer=user, article=article_id)
    commentMap = comment_wrraper(comments)
    return cors_http_response_json(commentMap)


@auth
def get_article_comments(request):
    dic = request.session["dic"]
    article_id = dic["article_id"]
    comments = Comment.objects.filter(article=article_id)
    contentMap = comment_wrraper(comments)
    return cors_http_response_json(contentMap)


# must check if user had added comment !
@auth
def add_comment(request):
    try:
        dic = request.session["dic"]
        article_id = dic["article_id"]
        user = request.user
        customers = Customer.objects.filter(user=user)
        if len(customers) <= 0:
            return cors_http_response("FAILED user doesn't exist")
        customer = customers[0]
        articles = Article.objects.filter(id=article_id)
        if len(articles) <= 0:
            return cors_http_response("FAILED article doesn't exist")
        article = articles[0]
        content = dic["content"]
        comments = Comment.objects.filter(customer=user, article=article)
        if len(comments) > 0:
            return cors_http_response("FAILED,comments already exits !")
        comment = Comment(customer=user, article=article, content=content)
        comment.save()
        return cors_http_response("OK")
    except Exception,e:
        return cors_http_response(unicode(e))


def cors_http_response(status):
    response = HttpResponse(json.dumps({"status": status}))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def cors_http_response_json(status):
    response = HttpResponse(status)
    response["Access-Control-Allow-Origin"] = "*"
    return response

 # calculate all type comment content's numbers
def comment_wrraper(comments):
    contentMap = {}
    for item in comments:
        content = item.content
        if not contentMap.__contains__(content):
            contentMap[content] = 1
        else:
            contentMap[content] += 1
    return json.dumps(contentMap)
