#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
        --disable-static \
        --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DSTROOT=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README.md")
