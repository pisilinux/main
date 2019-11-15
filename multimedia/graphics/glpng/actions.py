#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_STATIC_LIBS=OFF \
		                  -DCMAKE_INSTALL_LIBDIR=lib \
		                  ") 

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove static lib
    #pisitools.remove("/usr/lib/libglpng.a")
