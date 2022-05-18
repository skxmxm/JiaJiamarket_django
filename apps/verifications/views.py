from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.

class Captcha(View):
    def get(self, request, uuid):
        from libs.captcha.captcha import get_captcha
        text, img = get_captcha()
        from django_redis import get_redis_connection

        redis_cli = get_redis_connection('captcha')
        redis_cli.setex(uuid, 100, text)
        return HttpResponse(img, content_type='image/jpeg')
