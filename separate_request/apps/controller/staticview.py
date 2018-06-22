# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

from apps.controller import app, model

@app.route('/')
def hello():
    return '''<html><head></head><body>Hello World!<br />%s</body></html>''' % model.load()
