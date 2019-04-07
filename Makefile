install:
	pip3 install pychromecast
	pip3 install HTTPServer

start:
	python3 -m http.server 8888 & python3 ./listener.py
