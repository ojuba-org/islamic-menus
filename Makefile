
INSTALL=install

all:
# Convert scalable icons to png
	for i in 48 32 24 22 16; do \
		mkdir -p icons/$${i}x$${i}; \
		for j in icons/*.svg; do \
		  convert -background none $${j} -resize $${i}x$${i} icons/$${i}x$${i}/$$(echo $$(basename $${j}) | sed -e 's/svg$$/png/'); \
		done; \
	done

install:
	$(INSTALL) -d $(PREFIX)/etc/xdg/menus/applications-merged/
	$(INSTALL) -d $(PREFIX)/usr/share/desktop-directories/
	$(INSTALL) islamic.menu $(PREFIX)/etc/xdg/menus/applications-merged/
	$(INSTALL) *.directory  $(PREFIX)/usr/share/desktop-directories
	# Install icons
	$(INSTALL) -d $(PREFIX)/usr/share/icons/hicolor/scalable/categories
	$(INSTALL) icons/*.svg $(PREFIX)/usr/share/icons/hicolor/scalable/categories/
	for i in 48 32 24 22 16; do \
		$(INSTALL) -d $(PREFIX)/usr/share/icons/hicolor/$${i}x$${i}/categories; \
		$(INSTALL) icons/$${i}x$${i}/*.png $(PREFIX)/usr/share/icons/hicolor/$${i}x$${i}/categories/; \
	done

clean:
	# Clean png icons
	for i in 48 32 24 22 16; do \
		rm -rf icons/$${i}x$${i}; \
	done
