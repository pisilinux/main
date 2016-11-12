#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "pugixml-1.7/scripts"

def setup():    
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                                      -DBUILD_SHARED_LIBS=ON")

def build():    
    cmaketools.make()

def install():    
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")


