
INSTALL=install
po:
	make -C po all

in: po
	for i in *.in; do \
		intltool-merge -d po $${i} $${i/.in/}; \
	done

install: in
	$(INSTALL) -d $(PREFIX)/etc/xdg/menus/applications-merged/
	$(INSTALL) -d $(PREFIX)/usr/share/desktop-directories/
	$(INSTALL) -m 0644 islamic.menu $(PREFIX)/etc/xdg/menus/applications-merged/
	$(INSTALL) -m 0644 *.directory  $(PREFIX)/usr/share/desktop-directories
	# Install icons
	$(INSTALL) -d $(PREFIX)/usr/share/icons/hicolor/scalable/categories
	$(INSTALL) -m 0644 icons/*.svg $(PREFIX)/usr/share/icons/hicolor/scalable/categories/

