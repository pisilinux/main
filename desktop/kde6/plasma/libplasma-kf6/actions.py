#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools, get

def setup():
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()
    #set pisi-crocus-ancyrensis photos as default wallpapers
    pisitools.dosed("%s/usr/share/plasma/desktoptheme/default/plasmarc" % get.installDIR(), "Next", "pisi-crocus-ancyrensis")

    pisitools.dodoc("README.md")
