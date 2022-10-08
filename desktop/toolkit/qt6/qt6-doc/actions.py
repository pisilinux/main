#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get

def setup():
    qt6.configure()

def build():
    qt6.make("docs")
    # qt6.make("docs")

def install():
    qt6.install("install_docs")

    pisitools.dodoc("LICENSES/*")
