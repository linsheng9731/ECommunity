# coding:utf-8 #
__author__ = 'damon_lin'

from lib import *
import json
from models import *
import csv
import sys
from utils import auth


@auth
def add_record(request):
    data = '{"recorddata":[{"timestamp":"2015-06-16","readcount":"2","readspend":"0.00361111111"},{"timestamp":"2015-06-15","readcount":"2","readspend":"0.00361111111"},{"timestamp":"2015-06-14","readcount":"2","readspend":"0.00361111111"}],"sumreadcount":"6","sumreadspend":"0.04"}'
    try:
        data = json.loads(data)
        records = data["recorddata"]
        user = request.user
        customer = Customer.objects.filter(user=user)[0]
        for item in records:
            print(item)
            record = Record(timestamp=item["timestamp"], duration=item["readspend"], times=item["readcount"],
                            customer=customer)
            record.save()
        return HttpResponse(json.dumps({"status": "OK"}))
    except Exception, e:
        logger(e)


def get_record(requset):
    post = requset.POST
    start = post["start"]
    end = post["end"]
    records = Record.objects.filter(timestamp__range=(start, end))
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=' + unicode(start) + '_' + unicode(end) + '.csv'
    writer = csv.writer(response)
    for item in records:
        writer.writerow((item.customer.phone, item.timestamp,item.times, item.duration))
    return response