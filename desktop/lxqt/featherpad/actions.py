#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt5

# WorkDir = ""

def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README*", "NEWS")
