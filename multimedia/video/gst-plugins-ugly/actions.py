#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import get
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dpackage-name='PisiLinux gstreamer-plugins-ugly package' \
                          -Dpackage-origin='https://www.pisilinux.org'")

def build():
    mesontools.build()
    

def install():
    mesontools.install()

    pisitools.dodoc("README*", "COPYING", "AUTHORS", "NEWS")
