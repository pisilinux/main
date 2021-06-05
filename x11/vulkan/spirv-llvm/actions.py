#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DLLVM_INCLUDE_TESTS=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE*", "README*")
