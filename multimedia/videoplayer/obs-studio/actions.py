#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DCMAKE_C_COMPILER=gcc',
    ' -DCMAKE_CXX_COMPILER=g++',
    ' -DUNIX_STRUCTURE=ON',
    ' -DENABLE_JACK=ON',
    ' -DBUILD_VST=OFF',
    ' -DBUILD_BROWSER=OFF',
    ' -DOpenGL_GL_PREFERENCE=GLVND',
    ' -DENABLE_VLC=OFF',
    ' -DENABLE_LIBFDK=ON',
    ' -DENABLE_AJA=OFF',
    ' -DENABLE_NEW_MPEGTS_OUTPUT=OFF',
    ' -B_build -G Ninja -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    mesontools.build("-C _build")

def install():
    mesontools.install("-C _build")

    pisitools.dodoc("CONTRIBUTING*", "COPYING*", "README*")
