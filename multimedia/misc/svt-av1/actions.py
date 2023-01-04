#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DSVT_AV1_LTO=OFF',
    ' -DSVT_AV1_PGO=OFF',
    ' -DBUILD_TESTING=OFF -L '
    ])

def setup():
    pisitools.ldflags.add("-Wl,-z,noexecstack")
    cmaketools.configure(j)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG.md")
