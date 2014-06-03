homepage
========

A personal homepage using jinja templating and markdown for content.

Source borrowed from [Branden Ghena](https://github.com/brghena/brghena-homepage) who "gracefully stole" from [Pat Pannuto](https://github.com/ppannuto/patpannuto.com)


Requirements/Dependancies
-------------------------

Basically I'm pretty lazy and this is everything it took to make Branden's thing work in a fresh Ubuntu 14.04 VM

- Python3.4
	- sh
	- markdown
	- colorlog
	- jinja2
- PDFLaTeX
- Make

The deployment script is a dumb scp that I was messing with to see how yaml works.  It requires PyYaml, but if you're feeling like not using a dumb deployment script, you can change the deploy option in the Makefile to just do the scp you want.