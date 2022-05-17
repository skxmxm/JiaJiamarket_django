from django.urls import converters


class UsernameConverter:
    regex = '[0-9a-zA-Z_-]{5,20}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)


class MobileConverter:
    regex = r'1[345789]\d{9}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)
