# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

import os
import sys
import glob
from bottle import Bottle

import apps.models.somemodel
model = apps.models.somemodel.Somefunction()


app = Bottle()

_modules_ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]

for _module in _modules_:
    exec('import apps.controller.' + _module)
