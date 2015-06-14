# coding:utf-8 #
__author__ = 'damon_lin'
import json
import time
import requests
import urllib
import hashlib


def pushMessageAll(msg,type):
     # http://api.tuisong.baidu.com/rest/3.0/
    url = 'http://api.tuisong.baidu.com/rest/3.0/push/all'
    http_method = 'POST'
    opt = {"msg_type": type, "msg": msg, "device_type": 3,
           "timestamp": int(time.time()),"apikey":"EzBCvfmZTLqdOm1srdOKCR3N","expires":6000}
    opt["sign"] = _genSign(http_method, url, opt, "VSX2uaz6Vf5YRcyOk2Odv9u3Rtaw1V9I")

    headers = dict()

    headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
    headers['User-Agent'] = 'BCCS_SDK/3.0 (Darwin; Darwin Kernel Version 14.0.0: Fri Sep 19 00:26:44 PDT 2014; root:xnu-2782.1.97~2/RELEASE_X86_64; x86_64) PHP/5.6.3 (Baidu Push Server SDK V3.0.0 and so on..) cli/Unknown ZEND/2.6.0'

    return requests.post(url, data=opt, headers=headers)


def _genSign(method, url, arrContent,_secretKey):
    gather = method + url
    keys = arrContent.keys()
    keys.sort()
    for key in keys:
        gather += key + '=' + str(arrContent[key])
    gather += _secretKey
    sign = hashlib.md5(urllib.quote_plus(gather))
    return sign.hexdigest()

