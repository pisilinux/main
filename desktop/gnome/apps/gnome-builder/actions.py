#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dhelp=true \
                          -Dnetwork_tests=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "NEWS", "README.md", "COPYING")
