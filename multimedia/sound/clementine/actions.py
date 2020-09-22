#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_INSTALL_PREFIX=/usr \
     -DCMAKE_BUILD_TYPE=RelWithDebInfo \
     -DUSE_SYSTEM_TAGLIB=ON \
     -DENABLE_VK=ON \
    "

def setup():
    shelltools.system("sed -i 's|Exec=clementine %U|Exec=clementine|g' dist/clementine.desktop")
    cmaketools.configure(j)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("Changelog", "COPYING", "README*")

