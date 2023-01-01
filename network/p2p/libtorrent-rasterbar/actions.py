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
    pisitools.dosed("Makefile", "PREFIX=/usr/local/", "PREFIX=/usr")
    shelltools.system("mkdir build")
    shelltools.cd("build")
    cmaketools.configure("-GNinja .. \
                            -DCMAKE_SKIP_RPATH=TRUE \
                            -DCMAKE_CXX_STANDARD=17 \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_INSTALL_LIBDIR=lib \
                            -Dbuild_examples=ON \
                            -Dbuild_tests=ON \
                            -Dbuild_tools=ON \
                            -Dpython-bindings=ON \
                            -Dpython-egg-info=ON \
                            -Dpython-install-system-dir=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    #cmaketools.make()

#def check():
    #cmaketools.make("test")


def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    #cmaketools.rawInstall("DESTDIR=%s ninja install" % get.installDIR())

    shelltools.cd("..")
    pisitools.dohtml("docs/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "LICENSE")
