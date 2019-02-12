# Aristos Athens

'''
    Contact page
'''

import emailer
from captcha_generator import Captcha
from timeout import TimeOut


from flask import Blueprint
from flask import render_template
from flask import request

app = Blueprint("contact", __name__)
# captcha = captcha_generator.Captcha()

@app.route("/contact")
def index():
    html_file = __name__ + ".html"
    code, file_name = Captcha.generate_captcha()
    return render_template(html_file, captcha_code = code, captcha_file = file_name)

@app.route('/contact', methods=['POST'])
def my_form_post():
    sender = request.remote_addr
    if not TimeOut.timed_out(sender, __name__):
        return "You must wait before sending another message."
    else:
        TimeOut.add(sender, __name__, 5)

    sender = request.form['from']
    subject = request.form['subject']
    message = request.form['message']
    answer = request.form['answer']
    code = request.form['code']

    if Captcha.check_answer(code, answer):
        emailer.send_email(sender, subject, message)
        return "correct!"
    else:
        return "wrong!"
