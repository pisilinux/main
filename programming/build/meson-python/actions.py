#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -e '/ninja/d' -i pyproject.toml")
    # mesontools.configure("--prefix=/usr")

def build():
    python3modules.compile()
    # mesontools.build()

def install():
    python3modules.install()
    # mesontools.install()

    pisitools.dodoc("LICENSE", "README*")
