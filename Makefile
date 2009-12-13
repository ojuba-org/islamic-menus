
INSTALL=install

SOURCES=$(wildcard *.directory.in)
TARGETS=${SOURCES:.in=}

all: $(TARGETS)

pos:
	make -C po all

install: all
	$(INSTALL) -d $(PREFIX)/etc/xdg/menus/applications-merged/
	$(INSTALL) -d $(PREFIX)/usr/share/desktop-directories/
	$(INSTALL) -m 0644 islamic.menu $(PREFIX)/etc/xdg/menus/applications-merged/
	$(INSTALL) -m 0644 *.directory  $(PREFIX)/usr/share/desktop-directories
	# Install icons
	$(INSTALL) -d $(PREFIX)/usr/share/icons/hicolor/scalable/categories
	$(INSTALL) -m 0644 icons/*.svg $(PREFIX)/usr/share/icons/hicolor/scalable/categories/

%.directory: %.directory.in pos
	intltool-merge -d po $< $@

clean:
	rm -f $(TARGETS)
