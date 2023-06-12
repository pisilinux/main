#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools

def build():
    python3modules.compile()

def install():
    python3modules.install()
    pisitools.insinto("/usr/share/metainfo", "appimage/guiscrcpy.appdata.xml")
    pisitools.insinto("/usr/share/applications", "appimage/guiscrcpy.desktop")

    for size in ["128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "appimage/guiscrcpy-%s.png" % size, "guiscrcpy.png")

    # pisitools.insinto("", "")

    pisitools.dodoc("LICENSE", "README*")
