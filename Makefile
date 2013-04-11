SHELL = /bin/bash

PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/devconf.py
PUBLISHCONF=$(BASEDIR)/pubconf.py

html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	rm -fr $(OUTPUTDIR)

watch: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve: html
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

watch-serve: clean html
	@echo Starting up Pelican and SimpleHTTPServer
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) & \
	pelican_pid="$$!"; \
	cd $(OUTPUTDIR); \
	python -m SimpleHTTPServer || true; \
	kill $$pelican_pid

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages

.PHONY: html help clean watch serve watch-serve publish github
