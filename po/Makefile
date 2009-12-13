pot:
	intltool-update -g islamic-menus -p

po: pot
	for i in *.po; do \
		intltool-update -g islamic-menus -d $${i/.po/}; \
	done

all: po

