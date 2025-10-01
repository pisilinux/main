#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBLA_VENDOR=Generic \
                 -DCMAKE_INSTALL_PREFIX=/usr \
                 -DCMAKE_BUILD_TYPE=None \
                 -DNSTATIC=ON")

def build():
    cmaketools.make()

#def check():
    #cmaketools.make("test")


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # pisitools.dodoc("README*", "COPYING")

    pisitools.dodoc("LICENSE*", "README*")
