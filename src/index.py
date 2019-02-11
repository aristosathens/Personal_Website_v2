# Aristos Athens

'''
    Home page
'''

import atexit

import captcha_generator

from flask import Blueprint
from flask import render_template

app = Blueprint("index", __name__)
captcha = captcha_generator.Captcha()

@app.route("/")
def index():
    html_file = __name__ + ".html"
    name = "Aristos"
    code, file_name = captcha.generate_captcha()
    print(code)
    print(file_name)
    print(captcha._generate_captchas)
    return render_template(html_file, name = name)

