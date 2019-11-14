#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

#WorkDir = "fontforge-%s-b" % get.srcVERSION().split('_')[-1]

def setup():
    shelltools.export("PYTHON", "/usr/bin/python3")
    #pisitools.dosed("configure.ac", "fontforge_package_name", "fontforge")
    shelltools.system("./bootstrap --force")

    autotools.configure("--without-libuninameslist \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "LICENSE")

