#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/lxqt/themes/system")
    pisitools.remove("/usr/share/lxqt/themes/ambiance/Butterfly-Kenneth-Wimer.jpg")
    pisitools.remove("/usr/share/lxqt/themes/dark/wallpaper.png")
    pisitools.remove("/usr/share/lxqt/themes/frost/lxqt-origami-light.png")
    pisitools.remove("/usr/share/lxqt/themes/kde-plasma/kde-plasma.png")
    pisitools.remove("/usr/share/lxqt/themes/light/96640-simple_blue_widescreen.svg")
    pisitools.remove("/usr/share/lxqt/themes/light/simple_blue_widescreen.png")
