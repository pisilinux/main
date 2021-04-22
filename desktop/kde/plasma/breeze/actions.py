#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()
    
    #set pisi-crocus-ancyrensis photos as default wallpapers
    pisitools.dosed("%s/usr/share/plasma/look-and-feel/org.kde.breezedark.desktop/contents/defaults" % get.installDIR(), "Next", "pisi-crocus-ancyrensis")
    pisitools.dosed("%s/usr/share/plasma/look-and-feel/org.kde.breezetwilight.desktop/contents/defaults" % get.installDIR(), "Next", "pisi-crocus-ancyrensis")
