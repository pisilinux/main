#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# def setup():
    # cmaketools.configure("-DCMAKE_INSTALL_PREFIX='/usr' \
        # -DBUILD_SHARED_LIBS=On")

def build():
    autotools.make("-f makefile.shared IGNORE_SPEED=1")
    # cmaketools.make("-f makefile.shared IGNORE_SPEED=1")


def install():
    autotools.rawInstall("-f makefile.shared PREFIX=/usr DESTDIR=%s INSTALL_GROUP=root" % get.installDIR())
    # cmaketools.rawInstall("-f makefile.shared PREFIX=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README.md")
