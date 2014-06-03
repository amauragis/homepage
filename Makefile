SHELL := /bin/bash

all:
	./website.py
	$(MAKE) -C res
	mkdir -p html/res/
	cp -r res/*.pdf html/res/

local:	all
	pushd html && python3 -m http.server 8000; popd

deploy:	all
	./deploy.py

clean: 
	rm -rf html/
	rm -rf __pycache__
	$(MAKE) -C res clean

.PHONY: all local deploy clean
