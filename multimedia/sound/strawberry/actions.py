#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt


from pisi.actionsapi import cmaketools, pisitools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DENABLE_QT6=ON \
                          -DENABLE_PROJECTM=ON \
                          -DENABLE_MYGPO=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_POSITION_INDEPENDENT_CODE=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("README.md")
