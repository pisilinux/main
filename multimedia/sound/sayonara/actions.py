#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5
from pisi.actionsapi import get

def setup():
    kde5.configure("-DWITH_SYSTEM_TAGLIB=ON")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.remove("usr/share/icons/sayonara.png")
    pisitools.dodoc("CHANGES", \
    "LICENSE", \
    "MANUAL", \
    "README.md")

