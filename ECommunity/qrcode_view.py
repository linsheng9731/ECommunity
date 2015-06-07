# coding:utf-8 #
__author__ = 'damon_lin'
from lib import *
import  qrcode


def get_qrcode(request):
    post = request.POST
    content = post["content"]
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    filename = unicode(uuid.uuid1())
    qr.add_data("http://dhq.me/")
    qr.make(fit=True)
    img = qr.make_image()
    filename+=".png"
    img.save(filename)
    image = open(filename,"rb")
    buffer = image.read()
    image.close()
    os.remove(filename)
    return HttpResponse(buffer,content_type="image/jpeg")