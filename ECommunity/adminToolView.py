from ECommunity.models import Article, Channel, Collection
from utils import serializer
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

def tool_view(request):
    return render_to_response('adminTool.html')
