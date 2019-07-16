#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
	#shelltools.export("CXXFLAGS", '%s -DEXPDATADIR=\\\"/usr/share/abuse\\\"' % get.CXXFLAGS())
    #pisitools.dosed("src/sdlport/setup.cpp", "/var/games/abuse", "/usr/share/abuse")
    #autotools.configure("--datadir=/usr/share/abuse \
		                 #--with-x \
		                 #--enable-debug")
		                 
	cmaketools.configure("-DBUILD_SHARED_LIBS=OFF")

def build():
    cmaketools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.domove("/usr/share/games/abuse/*", "/usr/share/abuse/games/abuse/")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README.md", "TODO.md")
