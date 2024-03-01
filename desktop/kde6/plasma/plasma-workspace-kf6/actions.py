#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #shelltools.system("sed -i 's|5.11.0|5.10.0|g' CMakeLists.txt")
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()
    #pisitools.dosym("/usr/lib/drkonqi-kf6", "/usr/lib/libexec/drkonqi-kf6")
    
    pisitools.dosym("/usr/bin/startplasma-x11", "usr/bin/startkde")
    
    #set pisi-crocus-ancyrensis photos as default wallpapers
    pisitools.dosed("%s/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/defaults" % get.installDIR(), "Next", "pisi-crocus-ancyrensis")

    #set pisi-crocus-ancyrensis photos as default wallpapers
    #pisitools.dosed("%s/usr/share/plasma/look-and-feel/org.kde.breeze-kf6dark.desktop/contents/defaults" % get.installDIR(), "Next", "pisi-crocus-ancyrensis")
    #pisitools.dosed("%s/usr/share/plasma/look-and-feel/org.kde.breeze-kf6twilight.desktop/contents/defaults" % get.installDIR(), "Next", "pisi-crocus-ancyrensis")

    pisitools.dodoc("LICENSES/*")
