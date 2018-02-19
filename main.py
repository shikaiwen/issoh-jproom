import logging
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import g
app = Flask(__name__)

@app.route('/')
def start():

    return render_template('index.html')


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=80, debug=True)
#	app.run()