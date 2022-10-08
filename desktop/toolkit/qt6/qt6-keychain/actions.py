#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get


def setup():
    cmaketools.configure("-B build-qt6 -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt6/mkspecs/modules \
                          -DBUILD_WITH_QT6=ON")

def build():
    cmaketools.make("-C build-qt6")

def install():
    cmaketools.install("-C build-qt6 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "ReadMe*")

