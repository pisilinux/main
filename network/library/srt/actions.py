#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_STATIC=OFF \
                          -DENABLE_UNITTESTS=ON \
                          -DENABLE_GETNAMEINFO=ON \
                          -DUSE_ENCLIB=gnutls")

def build():
    cmaketools.make()

#def check():
    #cmaketools.make("test")


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
