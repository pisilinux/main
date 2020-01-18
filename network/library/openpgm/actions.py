#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.cd("openpgm/pgm/")
    shelltools.system("pwd")
    libtools.libtoolize("-fc")
    autotools.aclocal()
    autotools.autoheader()
    autotools.automake("--add-missing --copy")
    autotools.autoconf()
    # suppress c compiler warnings
    pisitools.cflags.add("-Wno-cpp -Wno-unused-result")
    autotools.configure()

def build():
    shelltools.cd("openpgm/pgm/")
    autotools.make()

def install():
    shelltools.cd("openpgm/pgm/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())