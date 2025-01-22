#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6
from pisi.actionsapi import kde5
from pisi.actionsapi import get

NoStrip=["/usr/share/icons"]
# TODO: kalgebra icon not shown in GUI
# TODO: more sub packages? *-libs etc.?

def setup():
    pisitools.cxxflags.add("-std=c++11 -pthread")
    # kde6.configure()
    kde5.configure()

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("LICENSES/*")
