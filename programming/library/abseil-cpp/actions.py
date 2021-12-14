#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-Bbuild \
                          -DABSL_ENABLE_INSTALL=ON \
                          -DCMAKE_BUILD_TYPE:STRING=None \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_CXX_STANDARD:STRING=17 \
                          -DBUILD_SHARED_LIBS=ON \
                          -DABSL_PROPAGATE_CXX_STD=ON")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "LICENSE", "README*")
