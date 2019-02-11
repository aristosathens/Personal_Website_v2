# Aristos Athens

'''
    About page
'''

from flask import Blueprint

app = Blueprint('about', __name__)

@app.route("/about")
def accountList():
    return "list of accounts"