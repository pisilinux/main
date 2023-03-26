#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import libtools

import os

datadir = "/usr/share/eboard"

def setup():
    libtools.libtoolize("--copy --force")

    autotools.configure("--prefix=/usr --man-prefix=/usr/share/man --extra-libs=dl")
    autotools.configure("-with-data-dir=%s" % datadir)

def build():
    autotools.make()

def install():
    pisitools.dodir(datadir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/man", "/usr/share")

    # pisitools.insinto("/usr/share/pixmaps", "icon-eboard.xpm")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
