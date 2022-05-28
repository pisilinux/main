#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

#WorkDir = "vokoscreenNG-%s/src" % get.srcVERSION()

def setup():
    pisitools.cxxflags.add("-Wno-deprecated-declarations")
    qt5.configure("src/vokoscreenNG.pro")

def build():
    qt5.make("PREFIX=/usr")

def install():
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    #pisitools.dobin("vokoscreenNG")
    #pisitools.insinto("/usr/share/applications", "src/applications/vokoscreenNG.desktop", "vokoscreenNG.desktop")
    #pisitools.insinto("/usr/share/pixmaps", "src/applications/vokoscreenNG.png", "vokoscreenNG.png")
    
    pisitools.dodoc("COPYING", "README.md")


