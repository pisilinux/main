#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX='/usr' \
        -DBUILD_SHARED_LIBS=On")

def build():
    cmaketools.make("-f makefile.shared")


def install():
    cmaketools.rawInstall("-f makefile.shared PREFIX=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README.md")
