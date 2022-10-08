#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get

def setup():
    qt6.configure()

def build():
    qt6.make()

def install():
    qt6.install()

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s-qt6" % bin)

    pisitools.dodoc("LICENSES/*")
