#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "\-DCMAKE_BUILD_TYPE=Release \
                -DFREEGLUT_BUILD_DEMOS=OFF \
              "

    if get.buildTYPE() == "emul32":

        shelltools.export("CFLAGS", "-m32")
        shelltools.export("CXXFLAGS", "-m32")

        options += "-DCMAKE_INSTALL_LIBDIR=lib32 -DFREEGLUT_BUILD_DEMOS=OFF \
                   "

    elif get.ARCH() == "x86_64":

        options += "-DCMAKE_INSTALL_LIBDIR=lib \
                   "
    
    pisitools.cflags.add("-fcommon")
    cmaketools.configure(options)

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README.md")
    # pisitools.dohtml("doc/*")
