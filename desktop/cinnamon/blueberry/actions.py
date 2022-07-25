#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.insinto("/etc/xdg/autostart/", "etc/xdg/autostart/blueberry-tray.desktop")
    pisitools.insinto("/usr", "usr/*")

    pisitools.dodoc("README*")