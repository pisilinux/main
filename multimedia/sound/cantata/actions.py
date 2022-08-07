#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools, cmaketools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_TOUCH_SUPPORT=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "LICENSE", "README", "TODO")

    pisitools.insinto("/usr/share/pixmaps/", "streams/icons/stream.png", "cantata.png")
