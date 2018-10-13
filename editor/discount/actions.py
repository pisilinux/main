#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools


def setup():
    shelltools.system("./configure.sh --prefix=/usr \
                                      --libdir=/usr/lib \
                                      --enable-all-features \
                                      --with-fenced-code \
                                      --shared")
    

def build():
    autotools.make()


def install():
    shelltools.system("sed -e 's|/sbin/ldconfig|/sbin/ldconfig -n|' -i librarian.sh")
    autotools.rawInstall("DESTDIR=%s install.everything" % get.installDIR())
    #pisitools.insinto("/", "usr")    
