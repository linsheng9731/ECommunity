# coding:utf8 #
__author__ = 'damon_lin'

from ECommunity.models import News
from rest_framework import serializers

class NewsSerializer(serializers.Serializer):

    title = serializers.CharField(allow_blank=True,max_length=100)

    content = serializers.CharField(allow_blank=True,max_length=300)
