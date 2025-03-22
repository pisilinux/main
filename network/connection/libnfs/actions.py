#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

y = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DENABLE_{UTILS,DOCUMENTATION}=ON',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(y)

def build():
    mesontools.build()

def install():
    mesontools.install()

    from pisi.actionsapi import shelltools, get
    for b in ["nfs-cat", "nfs-cp", "nfs-ls", "nfs-stat"]:
        shelltools.chmod("%s/usr/bin/%s" % (get.installDIR(), b), mode = 0755)

    for l in ["BSD", "GPL-3", "LGPL-2.1"]:
        pisitools.dodoc("COPYING", "LICENCE-%s.txt" % l)
