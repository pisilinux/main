#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_BUILD_TYPE=Release \
                            -DREGISTER_INSTALL_PREFIX=OFF \
                            -DBUILD_SHARED_LIBS=ON \
                            -DBUILD_STATIC_LIBS=ON \
                            -DBUILD_TESTING=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS*", "ChangeLog*", "COPYING*", "README*")
