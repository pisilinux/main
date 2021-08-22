#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

t = "./themes/*/gtk-2.0"

def setup():
	# do not build HighContrast theme.
	pisitools.dosed("themes/Makefile.am", "\ HighContrast", "")
	shelltools.system("sed -i '82a\ \ GtkMenuBar::window-dragging\ =\ 1' %s/main.rc" % t)
	shelltools.system("sed -i '83a\ \ GtkToolbar::window-dragging\ =\ 1' %s/main.rc" % t)
	shelltools.system("./autogen.sh --prefix=/usr")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.removeDir("/usr/share/locale")
	pisitools.dodoc("LICENSE", "NEWS", "README.md")

