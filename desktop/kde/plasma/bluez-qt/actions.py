#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():    
    kde5.configure("-DUDEV_RULES_INSTALL_DIR=/usr/lib/udev/rules.d")

def build():
    kde5.make()

def install():
    kde5.install()

    #pisitools.dodoc("README.md", "COPYING.LIB")
