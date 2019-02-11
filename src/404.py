# Aristos Athens

'''
    404 Redirect
'''

from flask import Blueprint
from flask import redirect
from flask import url_for

app = Blueprint("404", __name__)

@app.app_errorhandler(404)
def redirect_404(e):
    print("HERE")
    return redirect(url_for("index.index"))