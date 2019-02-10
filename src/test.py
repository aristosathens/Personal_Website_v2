# Aristos Athens

from flask import Flask # default http://127.0.0.1:5000/
from flask import request

# Flask object - Give __name__ to help Flask determine the root path
app = Flask(__name__)

'''
Routing (or mapping), we will connect each page to a function.
The return value is what the user will see. Eventually we will return some html.
For now, we return a string.
'''
# / is the root directory. The homepage.
@app.route("/")
def index():
    return "<h2>Homepage!</h2>"

@app.route("/about")
def about():
    return "<h1>About!<h1>"

'''
To pass variables from url, use angle brackets.
For example, user/Aristos and user/Emily. Both will call this function, and
    the variable username will contain 'Aristos' and 'Emily'.
'''
@app.route("/user/<username>")
def user(username):
    return username

'''
To pass integers, specify the type.
'''
@app.route("/integer/<int:number>")
def integer(number):
    return str(number)

'''
GET is the default way of getting/sending data.
'''
@app.route("/request")
def r():
    return "Method used: {}".format(str(request.method))

'''
Specifying list of methods says that this function can now handled both
    GET and POST.
To manually send a POST request, type: "curl -X POST http://127.0.0.1:5000/post"
'''
@app.route("/post", methods = ["GET", "POST"])
def post():
    if request.method == 'GET':
        return "This is using GET"
    if request.method == 'POST':
        return "This is using POST"




if __name__ == "__main__":
    app.run(debug = True) # start the app
