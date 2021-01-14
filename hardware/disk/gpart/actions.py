#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("Changes", "COPYING", "README.md")
