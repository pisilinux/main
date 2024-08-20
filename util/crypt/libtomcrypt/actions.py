#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def build():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CXXFLAGS())
    shelltools.export("CFLAGS", "%s -DLTM_DESC -DUSE_LTM  -fPIC" % get.CFLAGS())
    shelltools.system('export EXTRALIBS="-ltommath"')
    autotools.make("-f makefile.shared IGNORE_SPEED=1 library test")

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("-f makefile.shared DESTDIR=%s PREFIX=/usr INSTALL_GROUP='root'" % get.installDIR())
    pisitools.dodoc("LICENSE", "README.md")

