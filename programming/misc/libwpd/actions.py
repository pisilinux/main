#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    for f in ("AUTHORS", "NEWS", "ChangeLog"):
        shelltools.touch(f)

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")     

def build():
    autotools.make()

def install():
    autotools.install()
