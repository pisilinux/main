#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools, shelltools, cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX='/usr' \
        -DCMAKE_BUILD_TYPE='Release' \
        -DGSETTINGS_COMPILE=OFF \
        -DWITH_GTK=3 \
        -DCMAKE_INSTALL_LIBEXECDIR=lib/cpu-x")

def build():
    cmaketools.make()

#def check():
    #cmaketools.make("test")


def install():
    cmaketools.install()
    pisitools.dodoc("README*", "COPYING")
