#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DBUILD_TESTING=OFF", sourceDir="..")

def build():
    #shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.make()

def install():
    #shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "COPYING-CMAKE-SCRIPTS", "COPYING", "README.md", "COPYING.LIB")
