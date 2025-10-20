#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

j = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DUNIX_STRUCTURE=ON',
    ' -DOpenGL_GL_PREFERENCE=GLVND',
    ' -DBUILD_VST=ON',
    ' -DENABLE_{AJA,VLC,WEBSOCKET}=OFF',
    ' -DENABLE_JACK=ON',
    ' -DENABLE_LIBFDK=ON',
    ' -DENABLE_NEW_MPEGTS_OUTPUT=ON',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING")
