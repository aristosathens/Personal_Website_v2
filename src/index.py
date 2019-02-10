# Aristos Athens

'''
Home page
'''

from flask import Flask # default http://127.0.0.1:5000/
from flask import render_template

app = Flask(__name__, root_path = "./../")

@app.route("/")
def index():
    name = "Aristos"
    return render_template("index.html", name = name)

if __name__ == "__main__":
    app.run(debug = True)