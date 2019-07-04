#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
		                  -DBUILD_SHARED_LIBS=ON \
		                  -DBUILD_ALLEGRO4=OFF \
		                  -DBUILD_EXAMPLES=OFF \
		                  ")

def build():
    cmaketools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("*.md")
