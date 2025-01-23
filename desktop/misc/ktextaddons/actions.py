#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kde5
from pisi.actionsapi import kde6
from pisi.actionsapi import get


def setup():
    # cmaketools.configure("-B build -DBUILD_TESTING=OFF \
                                        # -DBUILD_DESIGNERPLUGIN=ON \
                                        # -DCMAKE_INSTALL_PREFIX=/usr \
                                        # -DCMAKE_INSTALL_LIBDIR=lib \
                                        # -DQT_MAJOR_VERSION=5 \
                                        # -DBUILD_QCH=ON")

    cmaketools.configure("-B build6 -DBUILD_TESTING=OFF \
                                        -DCMAKE_INSTALL_PREFIX=/usr \
                                        -DCMAKE_INSTALL_LIBDIR=lib \
                                        -DBUILD_DESIGNERPLUGIN=ON \
                                        -DBUILD_WITH_QT5:BOOL=OFF \
                                        -DBUILD_QCH=ON \
                                        -DQT_MAJOR_VERSION=6")
    # kde5.configure()

def build():
    # cmaketools.make("-C build")

    cmaketools.make("-C build6")

def install():
    # cmaketools.install("-C build")

    cmaketools.install("-C build6")

    pisitools.dodoc("LICENSES/*", "README*")
