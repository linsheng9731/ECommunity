# coding:utf-8 #
__author__ = 'damon_lin'
from lib import *
import  qrcode


def get_qrcode(request):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    qr.add_data("http://dhq.me/")
    qr.make(fit=True)
    img = qr.make_image()
    img.save("dhqme_qrcode.png")
    image = open("dhqme_qrcode.png","rb")
    return HttpResponse(image.read(),content_type="image/jpeg")