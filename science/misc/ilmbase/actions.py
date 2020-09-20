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
    shelltools.cd("IlmBase")
    shelltools.system("./bootstrap")
    autotools.configure("--disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.cd("IlmBase")
    autotools.make()

def check():
    shelltools.cd("IlmBase")
    autotools.make("check")

def install():
    shelltools.cd("IlmBase")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
