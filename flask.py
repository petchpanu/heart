# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:32:54 2020

@author: User
"""

import flask

# =============================================================================
# FLASK
# =============================================================================

app = flask.Flask(__name__)

@app.route("/")
def hello():
#    return "Hello World!"
    return '''<body>
<h2> Hello World !</h2>
    </body>
    '''
    
@app.route("/greet/<name>")
def greet(name):
    return "Hello, {}".format(name)

if __name__ == '__main__':
    app.run()