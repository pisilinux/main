#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools


def setup():
    kde6.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -DBUILD_TESTING=OFF")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("AUTHORS", "ChangeLog")

