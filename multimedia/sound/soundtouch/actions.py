#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX='/usr' \
        -DCMAKE_BUILD_TYPE=''")

def build():
    cmaketools.make()

#def check():
    #cmaketools.make("test")


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install docs
    pisitools.dodoc("COPYING.TXT", "README.html")
