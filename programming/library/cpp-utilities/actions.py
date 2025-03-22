#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, cmaketools, pisitools

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DUSE_STANDARD_FILESYSTEM=ON',
    ' -DFORCE_BOOST_IOSTREAMS_FOR_NATIVE_FILE_BUFFER=ON',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(i)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("LICENSE")
