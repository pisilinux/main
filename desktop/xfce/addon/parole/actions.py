#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

i = "-Dwayland=enabled \
     -Dx11=enabled \
     -Dtray-plugin=enabled \
     -Dnotify-plugin=enabled \
     -Dmpris2-plugin=enabled \
    "

def setup():
    mesontools.configure(i)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "NEWS", "README.md", "THANKS", "TODO")

