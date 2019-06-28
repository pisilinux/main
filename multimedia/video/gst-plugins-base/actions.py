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
    opts = {
            "introspection": "no" if get.buildTYPE() == "emul32" else "yes",
           }
    
    autotools.configure("--enable-introspection=%(introspection)s \
                         --with-package-name='PisiLinux gstreamer-plugins-base package' \
                         --with-package-origin='http://www.pisilinux.org' \
                         --disable-examples \
                        " % opts)
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
