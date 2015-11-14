#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools


def setup():
    kde5.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_BUILD_TYPE=Release")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING")