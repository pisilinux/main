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
    # Remove .c file to be regenerated from .defs file
    shelltools.unlink("src/pynotify.c")
    # suppress c compiler warnings
    pisitools.cflags.add("-Wno-deprecated-declarations -Wno-implicit-function-declaration")
    autotools.autoreconf("-fi")
    autotools.configure()
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())