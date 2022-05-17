from django.urls import path, register_converter
from apps.user.views import *
from utils.conventers import *
register_converter(UsernameConverter, 'username')
register_converter(MobileConverter, 'mobile')

urlpatterns = [
    path('usernames/<username:name>/count/', check_name),
    path('mobiles/<mobile:mobile>/count/', check_mobile),
    path('register/', register),
]
