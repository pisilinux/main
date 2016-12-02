#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import libtools

WorkDir = "MediaInfo"

def setup():
    for it in ["Project/GNU/CLI", "../GUI"]:
        configure_args = " --with-wxwidgets --with-wx-gui" if it.endswith('GUI') else ""
        shelltools.cd(it)
        libtools.libtoolize("--automake")
        autotools.aclocal()
        autotools.automake("-afc")
        autotools.autoconf()
        autotools.configure("--disable-static%s" % configure_args)

def build():
    for it in ["Project/GNU/CLI", "../GUI"]:
        shelltools.cd(it)
        autotools.make("-j1")

def install():
    pisitools.dodoc("*.txt")
    pisitools.dohtml("*.html")
    pisitools.insinto("/usr/share/pixmaps", "Source/Resource/Image/MediaInfo.png", "mediainfo.png")
    pisitools.insinto("/usr/share/icons/hicolor/128x128/apps/", "Source/Resource/Image/MediaInfo.png", "mediainfo.png")
    for it in ["Project/GNU/CLI", "../GUI"]:
        shelltools.cd(it)
        autotools.install()
        if it.endswith('GUI'): pisitools.insinto("/usr/share/applications", "mediainfo-gui.kde4.desktop")
