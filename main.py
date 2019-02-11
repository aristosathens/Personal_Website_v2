# Aristos Athens

'''
    Entry point for Flask application.
'''

import sys
from os import listdir
from importlib import import_module

from flask import Flask # default http://127.0.0.1:5000/
from flask import render_template

from flask import redirect
from flask import url_for


def register_pages(main_app, directory = "src/", ending = ".py"):
    '''
        Imports all modules in directory.
        If module has object named app, add this to main_app.
        app must be a Flask Blueprint object.
    '''
    sys.path.insert(0, directory)
    files = listdir(directory)
    files = [file[:-len(ending)] for file in files]
    print(files)
    for module_name in files:
        try:
            module = import_module(module_name)
            blueprint = getattr(module, "app")
            main_app.register_blueprint(blueprint)
        except:
            print("Skipping file: " + module_name)


if __name__ == "__main__":
    app = Flask(__name__)
    register_pages(app, ending = ".py", directory = "src/")
    app.run(debug = True)
else:
    raise Exception("Error: Why are you importing main.py?")