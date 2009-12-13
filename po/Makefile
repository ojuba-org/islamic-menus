POTFILE=$(shell cat POTFILES.in)
SOURCES=$(addprefix ../, $(POTFILE))

all: $(wildcard *.po)

islamic-menus.pot: $(SOURCES)
	intltool-update -g islamic-menus -p

%.po: islamic-menus.pot
	intltool-update -g islamic-menus -d $*
