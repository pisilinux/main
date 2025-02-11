#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools, get

i = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DREDIS_STORAGE_BACKEND=OFF',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(i)

def build():
    mesontools.build()

def check():
#    mesontools.build("test")
    pass

def install():
    mesontools.install()

    # Create symlinks
    for cc in ("gcc", "g++", "cc", "c++"): # , "clang" , "clang++"
        pisitools.dosym("/usr/bin/ccache", "/usr/lib/ccache/bin/%s" % cc)
        pisitools.dosym("/usr/bin/ccache", "/usr/lib/ccache/bin/%s-%s" % (get.HOST(), cc))

    pisitools.dodoc("GPL-3.0.txt", "LGPL-3.0.txt")
