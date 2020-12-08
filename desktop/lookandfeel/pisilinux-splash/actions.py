#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/com.gitlab.jurassicplayer.SnowyNightMiku/org.kde.sweet-cat.desktop/g' metadata.json")
    
    shelltools.cd("../pisilinux.splash-0.1")
    shelltools.system("sed -i 's/com.gitlab.jurassicplayer.SnowyNightMiku/org.kde.pisilinux.desktop/g' metadata.json")
    #autotools.configure()

#def build():
    #autotools.make()

def install():
    shelltools.cd("../pisilinux.splash-0.1")
    pisitools.insinto("/usr/share/plasma/look-and-feel/org.kde.pisilinux.desktop", "*")
    
    shelltools.cd("../Sweet-Cat_Animated-0.1")
    pisitools.insinto("/usr/share/plasma/look-and-feel/org.kde.sweet-cat.desktop", "*")
