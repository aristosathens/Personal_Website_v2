# Aristos Athens

'''
    Contact page
'''

import captcha_generator

from flask import Blueprint
from flask import render_template
from flask import request

app = Blueprint("contact", __name__)
captcha = captcha_generator.Captcha()

@app.route("/contact")
def index():
    html_file = __name__ + ".html"
    code, file_name = captcha.generate_captcha()
    print("file_name: ", file_name)
    return render_template(html_file, captcha_code = code, captcha_file = file_name)

@app.route('/contact', methods=['POST'])
def my_form_post():
    answer = request.form['text']
    code = request.form['code']
    if captcha.check_answer(code, answer):
        return "correct!"
    else:
        return "wrong!"
