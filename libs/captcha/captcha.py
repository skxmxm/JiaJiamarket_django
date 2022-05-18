import random
import string
from captcha.image import ImageCaptcha
import os


def get_captcha():
    content = string.digits + string.ascii_lowercase

    letter = random.sample(content, 5)
    cap_str = "".join(letter)

    img_captcha = ImageCaptcha()
    img = img_captcha.generate_image(cap_str)
    img.save('./libs/captcha/image/' + cap_str + '.jpg')
    with open('./libs/captcha/image/' + cap_str + '.jpg', 'rb') as file:
        img_bytes = file.read()
    os.remove('./libs/captcha/image/' + cap_str + '.jpg')
    img.tobytes()
    return cap_str, img_bytes
