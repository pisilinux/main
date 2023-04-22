#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dskip_dbus_tests=true \
                          -Dskip_gtk_tests=true  \
                          -Dprofiler=disabled \
                          -Dinstalled_tests=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("CONTRIBUTING.md", "COPYING", "NEWS", "README.md")
