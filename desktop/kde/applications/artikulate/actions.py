#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import kde6

def setup():
    cmaketools.configure("-B build -DBUILD_TESTING=OFF \
                                        -DKDE_INSTALL_LIBDIR=lib \
                                        -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("COPYING*")
