#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", "clang")
    shelltools.export("CXX", "clang++")

    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DOCLICD_COMPAT=1")

def build():
    cmaketools.make()

def install():

    autotools.rawInstall("DESTDIR=%s" %get.installDIR())
    pisitools.remove("/usr/include/CL/*")
    pisitools.removeDir("/usr/include")

