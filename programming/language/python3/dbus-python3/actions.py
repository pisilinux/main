#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "-lpthread")
    mesontools.configure("-Ddoc=disabled")
    
    # pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    mesontools.build()


def check():
    #autotools.make("check")
    pass

def install():
    mesontools.install()

    # remove dbus-python-common files in py3 package
    pisitools.removeDir("/usr/include/")
    pisitools.removeDir("/usr/lib/pkgconfig")
    #pisitools.removeDir("/usr/share/")
