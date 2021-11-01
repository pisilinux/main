#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("patch -p1 -R < bdc281eadb1d58d5c0c7bbc1125ee4674256df08.patch")

    shelltools.system("./bootstrap.sh")
    
    autotools.configure("--disable-static \
                         --with-fontconfig \
                         --with-png \
                         --with-freetype \
                         --with-jpeg \
                         --without-xpm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml(".")
    pisitools.dodoc("COPYING", "README*")
