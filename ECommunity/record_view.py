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
    dic = request.session["dic"]
    data = dic["data"]
    # data = '{"recorddata":[{"timestamp":"2015-06-16","readcount":"2","readspend":"0.00361111111"},{"timestamp":"2015-06-15","readcount":"2","readspend":"0.00361111111"},{"timestamp":"2015-06-14","readcount":"2","readspend":"0.00361111111"}],"sumreadcount":"6","sumreadspend":"0.04"}'
    try:
        data = json.loads(data)
        records = data["recorddata"]
        user = request.user
        customer = Customer.objects.filter(user=user)[0]
        total_duration = 0
        total_times = 0
        for item in records:
            print(item)
            record = Record(timestamp=item["timestamp"], duration=item["readspend"], times=item["readcount"],
                            customer=customer)
            record.save()
            total_duration += float(item["readspend"])
            total_times += float(item["readcount"])

        customer_times = float(customer.total_times)
        customer_durations = float(customer.total_durations)
        customer_times += total_times
        customer_durations += total_duration
        customer.total_times = unicode(customer_times)
        customer.total_durations = unicode(customer_durations)
        customer.save()
        return HttpResponse(json.dumps({"sumreadcount": customer_times,"sumreadspend":customer_durations}))
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
        writer.writerow((item.customer.phone, item.timestamp, item.times, item.duration))
    return response