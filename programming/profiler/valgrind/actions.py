#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-ifv")
    shelltools.export("CFLAGS", get.CFLAGS().replace("-fstack-protector",""))
    shelltools.export("CPPFLAGS", get.CXXFLAGS().replace("-fstack-protector",""))
    autotools.configure("--without-mpicc --libexecdir=/usr/lib")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "FAQ.txt", "NEWS", "README*")
