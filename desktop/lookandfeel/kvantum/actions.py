#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools, get

WorkDir = "Kvantum-%s/Kvantum" % get.srcVERSION()

def setup():
    pisitools.dosed("style/CMakeLists.txt", "Qt5\ Qt6", "Qt6")
    cmaketools.configure("-DENABLE_QT5=ON -B_build5 -G Ninja")
    cmaketools.configure("-DENABLE_QT5=OFF -B_build6 -G Ninja")

def build():
    mesontools.build("-C _build5")
    mesontools.build("-C _build6")

def install():
    mesontools.install("-C _build5")
    mesontools.install("-C _build6")

    pisitools.dodoc("ChangeLog")
