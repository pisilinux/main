#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():

    cmaketools.configure("--prefix=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("README.md", "LICENSE.txt")
