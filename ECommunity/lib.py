# coding:utf8 #
__author__ = 'damon_lin'

from django.contrib.auth.decorators import login_required
from ECommunity.models import Customer,Channel,Article
from django.http import HttpResponse
import json
import string
import random
import urllib
import urllib2
import re