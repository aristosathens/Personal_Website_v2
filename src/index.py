# Aristos Athens

'''
    Home page
'''

from flask import Blueprint
from flask import render_template

app = Blueprint("index", __name__)

@app.route("/")
def index():
    html_file = __name__ + ".html"
    name = "Aristos"
    return render_template(html_file, name = name, banner_image = "banner_example.jpg")

