#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools, get

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()
    #set pisi-crocus-ancyrensis photos as default wallpapers
    pisitools.dosed("%s/usr/share/plasma/desktoptheme/default/plasmarc" % get.installDIR(), "Next", "pisi-crocus-ancyrensis")

    pisitools.dodoc("README.md")
