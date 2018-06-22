# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

.PHONY : clean
clean:
	rm -rf __pycache__/
	rm -rf */__pycache__/
	rm -rf */*/__pycache__/
	rm -rf ./*.pyc
	rm -rf */*.pyc
	rm -rf */*/*.pyc


.PHONY : start
start:
	@python3 serv.py &
	@echo '[*] Start service program.'


.SILENT:
stop:
	-@pkill -f serv.py | true
	@echo '[*] Stop service program.'


.PHONY : pid
pid:
	-@ps u | grep 'python3 serv.py' | grep -v grep
