#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #shelltools.system("sed -i '115d; 121,137d; 139,140d'  configure.ac")
    #shelltools.system("sed -i '/valadoc/d' Makefile.am")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-valadoc \
                         --with-pic")
    
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS", "README", "AUTHORS", "COPYING")
