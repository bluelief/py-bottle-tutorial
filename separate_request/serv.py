# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

from apps.controller import *
import bjoern

bjoern.run(app, host='localhost', port=8080)
