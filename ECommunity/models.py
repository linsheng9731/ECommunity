# coding:utf8 #
__author__ = 'damon_lin'

from django.db import models

class News(models.Model):

    title = models.CharField(max_length=100)

    content = models.CharField(max_length=300)

#用户
class Customer(models.Model):

    User_Phone = models.CharField(max_length=100)

    User_NickName = models.CharField(max_length=100)

    User_Sex = models.CharField(max_length=100)

    User_PicURL	= models.CharField(max_length=100)

    User_Grade = models.CharField(max_length=100)

#频道
class Channel(models.Model):

    #Channel_ID = models.CharField(max_length=100)

    Channel_Name = models.CharField(max_length=100)

    Type_ID = models.CharField(max_length=100)

    Channel_Num = models.CharField(max_length=100)

    Channel_Cata = models.CharField(max_length=100)

    Channel_Desc = models.CharField(max_length=100)

    Channel_PicURL = models.CharField(max_length=100)

#文章
class article(models.Model):

    #Article_ID

    Article_author = models.CharField(max_length=100)

    Article_Title = models.CharField(max_length=100)

    Article_Body = models.TextField()

    Article_Logo_pic = models.CharField(max_length=100)

    # which channel the article belong to #
    Article_channel_ID = models.ForeignKey(Channel)

    Article_Desc = models.TextField()

    Article_Create_time = models.CharField(max_length=100)

    Article_Create_modify = models.CharField(max_length=100)