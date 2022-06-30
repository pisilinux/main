#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("-D enable-installed-tests=false")

def build():
    mesontools.build

def install():
    mesontools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING.LIB", "NEWS", "README")
