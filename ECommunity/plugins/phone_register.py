# coding:utf8 #
__author__ = 'damon_lin'

from django.contrib.auth import *
from django.contrib.auth.views import *
from django.contrib.auth.models import User
from datetime import *
from ECommunity.lib import *


VERIFY_PHONE_URL = 'http://106.ihuyi.cn/webservice/sms.php?method=Submit'

def random_dig(length=4):
    str = ''
    for i in range(length):
        str += (random.choice('1234567890'))
    return str

# 检验是否存在用户
def is_phone_exists(request):
    phone = request.POST['phonenum']
    try:
        customer = Customer.objects.get(phone=phone)
        return HttpResponse(json.dumps({'state': 'USER EXISTS'}))
    except:
        return HttpResponse(json.dumps({'state': 'SUCCESS'}))

# 发送验证码
def begin_phone_verify(request):
    phone = request.POST['phonenum']
    try:
        customer = Customer.objects.get(phone=phone)
    except:
        pass
    # if isinstance(customer, Customer):
    # return HttpResponse(json.dumps({'state': 'USER EXISTS'}))

    verification_code = random_dig()
    print verification_code, '----------------------'
    request.session['phone_verify'] = verification_code
    request.session['phone_number'] = phone
    verify_data = {'account': 'cf_quletao', 'password': 'qlt10905qlt',
                   'mobile': phone, 'content': '闲着-中老年人休闲生活服务平台，验证码：'+verification_code}
    verify_data_urlencode = urllib.urlencode(verify_data)
    req = urllib2.Request(url=VERIFY_PHONE_URL, data=verify_data_urlencode)

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res,'-----',type(res)
    rer = re.compile(r'(?<=<code>)(.+?)(?=</code>)').search(res)
    print rer.group(1)
    # if rer.group(1) == '2':
    #     return HttpResponse(json.dumps({'state': '2'}))
    # elif rer.group(1) == '0':
    #     return HttpResponse(json.dumps({'state': '0'}))
    # elif rer.group(1) == '403':
    #     return HttpResponse(json.dumps({'state': '403'}))
    # else:
    #     return HttpResponse(json.dumps(({'state': 'UNKNOWN ERROR'})))

    # return render(request, website.phone_verify)
    return HttpResponse(json.dumps({'state': 'SUCCESS'}))

# 校验验证码
def phone_verify(request):
    pwd = request.POST['pwd']
    verification_code = request.POST['verification_code']
    if verification_code == request.session['phone_verify']:
        phone = request.session['phone_number']
        date = datetime.now()

        u = User.objects.filter(username=phone)
        if len(u)>0:  # 假如用户已经存在 直接更新密码
            u = u[0]
            if u is not None:
                u.set_password(pwd)
                u.save()
                return HttpResponse(json.dumps({'state': 'SUCCESS'}))

        u = User.objects.create_user(phone, "", pwd);
        try:
            pass
            u.save()
            customer = Customer(user=u, phone=phone, nickname=phone)
            customer.save()
            u = authenticate(username=phone, password=pwd)
        except Exception, e:
            print(e)
            raise e
            return HttpResponse("error")
        if u is not None:
            pass
            login(request, u)
            del request.session['phone_number']
            del request.session['phone_verify']
            return HttpResponse(json.dumps({'state': 'SUCCESS'}))
        else:
            return HttpResponse(json.dumps({'state': 'FAILED'}))
    else:
        # del request.session['phone']
        # del request.session['phone_verify']
        return HttpResponse(json.dumps({'state': 'FAILED'}))

# 验证用户
def userLogin(request):
    name = request.POST["phonenum"]
    pws = request.POST["pwd"]

    user = authenticate(username=name, password=pws)
    if user is not None:
        login(request, user)
        return HttpResponse(json.dumps({'state': 'SUCCESS'}))
    else:
        return HttpResponse(json.dumps({'state': 'FAILED'}))


# 重置密码
def resetPassword(request):
    pws = request.POST["pwd"]
    user = request.user
    user.set_password(pws)
    user.save()
    return HttpResponse("reset succeed!")


def is_login(user):
    return user.is_authenticated()

def user_register(request):
    phone = request.POST.get('phone')
    pwd = request.POST.get('pwd')
    date = datetime.now()
    new_user = User.objects.create_user(phone, phone, pwd)
    try:
        new_user.save()
    except:
        # return a error to front page
        return HttpResponse('register error')
    return HttpResponse(json.dumps({"state": "SUCCESS"}))
