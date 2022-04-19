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
   
   #fixed menu icon for Pisi
    light_themes=("Clearlooks","KDE-Plasma", "light", "system")
    for i in light_themes:
        pisitools.remove("/usr/share/lxqt/themes/%s/mainmenu.svg" % i)
        pisitools.dosym("/usr/share/icons/hicolor/scalable/places/start-here-light.svg", "/usr/share/lxqt/themes/%s/mainmenu.svg" % i)

    dark_themes=("ambiance", "Arch-Colors", "dark", "frost", "Leech", "silver", "Valendas")
    for i in dark_themes:
        pisitools.remove("/usr/share/lxqt/themes/%s/mainmenu.svg" % i)
        pisitools.dosym("/usr/share/icons/hicolor/scalable/places/start-here-dark.svg", "/usr/share/lxqt/themes/%s/mainmenu.svg" % i)

    pisitools.remove("/usr/share/lxqt/themes/kvantum/lxqt-panel/mainmenu.svg")
    pisitools.dosym("/usr/share/icons/hicolor/scalable/places/start-here-dark.svg", "/usr/share/lxqt/themes/kvantum/lxqt-panel/mainmenu.svg")
