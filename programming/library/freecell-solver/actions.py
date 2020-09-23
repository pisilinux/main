#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DFCS_WITH_TEST_SUITE=OFF \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_SKIP_BUILD_RPATH=ON \
                          -DBUILD_STATIC_LIBRARY=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING.asciidoc", "README.asciidoc")