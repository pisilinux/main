#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

NoStrip=["/usr/share/icons"]
# TODO: KAlgebra icon not shown in GUI
# TODO: more sub packages? *-libs etc.?

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING*", "DESIGN", "README.md", "TODO")
