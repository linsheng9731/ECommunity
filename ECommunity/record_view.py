# coding:utf-8 #
__author__ = 'damon_lin'

from lib import *
import json
from models import *

def add_record(request):
    data = '{"phonenum":"18767121895","password":"123456","readcount":[{"timestamp":"2015-06-16","recorddata":"2"},{"timestamp":"2015-06-15","recorddata":"6"},{"timestamp":"2015-06-14","recorddata":"9"}],"readspend":[{"timestamp":"2015-06-13","recorddata":"0.039444444444444435"},{"timestamp":"2015-06-14","recorddata":"0.016666666666666666"},{"timestamp":"2015-06-15","recorddata":"0.006388888888888889"},{"timestamp":"2015-06-16","recorddata":"0.0036111111111111114"}]}'
    try:
        data = json.loads(data)
        records = data["readcount"]
        for item in records:
            print(item)
            record = Record(timestamp=item["timestamp"],duration=item["recorddata"])
            record.save()
        return HttpResponse(json.dumps({"status":"OK"}))
    except Exception,e:
        logger(e)

