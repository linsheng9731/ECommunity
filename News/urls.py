# coding:utf8 #
__author__ = 'damon_lin'
from django.conf.urls import include, url
from django.contrib import admin
from News.NewsViewSet import NewsViewSet
from rest_framework.routers import DefaultRouter

# news_list = NewsViewSet.as_view({
#      'getbyid': 'getbyid'
# })

router = DefaultRouter()
router.register(r'^news',NewsViewSet)
urlpatterns = [
    # Examples:
    # url(r'^$', 'ECommunity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^news','News.views.list_news'),
    #url(r'^news', news_list),
    url(r'^',include(router.urls)),
]


