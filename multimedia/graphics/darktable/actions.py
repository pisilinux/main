#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools, pisitools

j = ''.join([
    ' -DUSE_COLORD=ON',
    ' -DUSE_OPENJPEG=ON',
    ' -DUSE_LIBSECRET=ON',
    ' -DBUILD_USERMANUAL=1',
    ' -DENABLE_RAWSPEED=ON',
    ' -DRAWSPEED_ENABLE_LTO=ON',
    ' -DBINARY_PACKAGE_BUILD=1',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_LIBDIR=/usr/lib',
    ' -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib',
    ' -B_build -G Ninja -L '
    ])

def setup():
    pisitools.ldflags.add("-lgs")
    cmaketools.configure(j)

def build():
    mesontools.build("-C _build")

def install():
    mesontools.install("-C _build")
    
    # fix libdarktable.so path under /usr/lib
    pisitools.dosym("/usr/lib/darktable/libdarktable.so", "/usr/lib/libdarktable.so")
