#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

i = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -Dsctp_build_shared_lib=1',
    ' -DPREFER_SYSTEM_LIBS=ON',
    ' -DUSE_SYSTEM_{PLOG,SRTP,JUICE,USRSCTP,JSON}=1',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(i)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("LICENSE")
