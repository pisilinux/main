#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, shelltools, pisitools

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DUNIT_TESTING=ON',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(i)

def build():
    mesontools.build()

    shelltools.cd("doc")
    shelltools.system("doxygen mainpage.dox")
    
def check():
    mesontools.build("-C build test")

def install():
    mesontools.install()

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("AUTHORS", "COPYING")
