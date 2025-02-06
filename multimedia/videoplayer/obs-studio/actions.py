#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, mesontools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DCMAKE_C_COMPILER=gcc',
    ' -DCMAKE_CXX_COMPILER=g++',
    ' -DUNIX_STRUCTURE=ON',
    ' -DOpenGL_GL_PREFERENCE=GLVND',
    ' -DBUILD_VST=ON',
    ' -DENABLE_{AJA,VLC,BROWSER}=OFF',
    ' -DENABLE_JACK=ON',
    ' -DENABLE_LIBFDK=ON',
    ' -DENABLE_NEW_MPEGTS_OUTPUT=ON',
    ' -B_build -G Ninja -L '
    ])

def setup():
    for b in ["browser", "websocket"]:
        shelltools.touch("plugins/obs-%s/CMakeLists.txt" % b)
    cmaketools.configure(j)

def build():
    mesontools.build("-C _build")

def install():
    mesontools.install("-C _build")

    pisitools.dodoc("AUTHORS", "COPYING")
