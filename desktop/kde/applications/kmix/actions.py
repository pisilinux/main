#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6
from pisi.actionsapi import kde5

NoStrip=["/usr/share"]

def setup():
    # kde6.configure("-Dkmix_KF5_BUILD=ON")
    kde5.configure("-Dkmix_KF5_BUILD=ON")

def build():
    kde6.make()

def install():
    kde6.install()
