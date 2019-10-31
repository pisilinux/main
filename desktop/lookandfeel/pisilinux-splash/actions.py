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
    shelltools.system("sed -i 's/com.gitlab.jurassicplayer.SnowyNightMiku/org.kde.pisilinux.desktop/g' metadata.json")
    #autotools.configure()

#def build():
    #autotools.make()

def install():
    pisitools.insinto("/usr/share/plasma/look-and-feel/org.kde.pisilinux.desktop", "*")
