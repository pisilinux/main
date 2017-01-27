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
    shelltools.makedirs("build-python3")
    autotools.autoreconf("-fi")

    shelltools.cd("build-python3")
    shelltools.system("PYTHON=python3 ../configure --prefix=/usr \
                       --localstatedir=/var \
                       --disable-api-docs \
                       --disable-html-docs \
                       --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.cd("build-python3")
    autotools.make()


def check():
    #autotools.make("check")
    pass

def install():
    shelltools.cd("build-python3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove dbus-python-common files in py3 package
    pisitools.removeDir("/usr/include/")
    pisitools.removeDir("/usr/lib/pkgconfig")
    pisitools.removeDir("/usr/share/")
