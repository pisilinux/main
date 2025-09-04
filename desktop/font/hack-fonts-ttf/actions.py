#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    pisitools.insinto("/usr/share/fonts/TTF", "build/ttf/Hack-*.ttf")
    pisitools.insinto("/etc/fonts/conf.avail/45-Hack.conf", "config/fontconfig/45-Hack.conf")

    pisitools.dosym("/etc/fonts/conf.avail/45-Hack.conf", "/etc/fonts/conf.d/45-Hack.conf")

    pisitools.dodoc("LICENSE.md", "README.md")
