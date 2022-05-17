import json
import re

from django.shortcuts import render
from django.http import JsonResponse
from apps.user.models import *
from django.views import View


# Create your views here.
def check_name(request, name):
    count = User.objects.filter(username=name).count()
    if count == 0:
        return JsonResponse({'code': 0, 'errmsg': 'ok', 'count': count})
    else:
        return JsonResponse({'code': 400, 'errmsg': 'found identical name', 'count': count})


def check_mobile(request, mobile):
    count = User.objects.filter(phone=mobile).count()
    if count == 0:
        return JsonResponse({'code': 0, 'errmsg': 'ok', 'count': count})
    else:
        return JsonResponse({'code': 400, 'errmsg': 'found identical name', 'count': count})


def register(request):
    body = request.body.decode()
    data_dict = json.loads(body)
    username = data_dict.get('username')
    password = data_dict.get('password')
    password2 = data_dict.get('password2')
    mobile = data_dict.get('mobile')
    allow = data_dict.get('allow')
    if not all([username, password, password2, mobile, allow]):
        return JsonResponse({'code': 400, 'errmsg': 'found empty data'})
    elif not re.match('[0-9a-zA-Z_-]{5,20}', username):
        return JsonResponse({'code': 400, 'errmsg': 'username is invalid'})
    elif User.objects.filter(username=username).count():
        return JsonResponse({'code': 400, 'errmsg': 'username is used'})
    elif not re.match(r'[0-9a-zA-Z_-]{8,20}', password) or not re.match(r'[0-9a-zA-Z_-]{8,20}', password2):
        return JsonResponse({'code': 400, 'errmsg': 'password is invalid'})
    elif password != password2:
        return JsonResponse({'code': 400, 'errmsg': 'passwords are different'})
    elif not re.match(r'^1[345789]\d{9}$', mobile):
        return JsonResponse({'code': 400, 'errmsg': 'mobile number is invalid'})
    elif User.objects.filter(phone=mobile).count():
        return JsonResponse({'code': 400, 'errmsg': 'mobile number is used'})
    elif not allow:
        return JsonResponse({'code': 400, 'errmsg': 'certificate is not allowed'})
    else:
        User.objects.create_user(username=username, password=password, phone=mobile)
        return JsonResponse({'code': 0, 'errmsg': 'ok'})
