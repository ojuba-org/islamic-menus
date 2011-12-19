DESTDIR?=/
sysconfdir?=$(DESTDIR)/etc
datadir?=$(DESTDIR)/usr/share
INSTALL=install

SOURCES=$(wildcard *.directory.in)
TARGETS=${SOURCES:.in=}

all: $(TARGETS)

pos:
	make -C po all

install: all
	$(INSTALL) -d $(sysconfdir)/xdg/menus/applications-merged/
	$(INSTALL) -d $(sysconfdir)/xdg/menus/applications-gnome-merged/
	$(INSTALL) -m 0644 islamic.menu $(sysconfdir)/xdg/menus/applications-merged/
	$(INSTALL) -m 0644 islamic.menu $(sysconfdir)/xdg/menus/applications-gnome-merged/
	$(INSTALL) -d $(datadir)/desktop-directories/
	$(INSTALL) -m 0644 *.directory  $(datadir)/desktop-directories
	# Install icons
	$(INSTALL) -d $(datadir)/icons/hicolor/scalable/categories
	$(INSTALL) -m 0644 icons/*.svg $(datadir)/icons/hicolor/scalable/categories/

%.directory: %.directory.in pos
	intltool-merge -d po $< $@

clean:
	rm -f $(TARGETS)
