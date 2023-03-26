#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.copytree("%s/usr/share/pkgconfig" % get.installDIR(), "%s/usr/lib/pkgconfig" % get.installDIR())
    pisitools.removeDir("/usr/share/pkgconfig")

    pisitools.dodoc("README.md", "LICENSES/*")
