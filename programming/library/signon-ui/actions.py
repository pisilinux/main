#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt6, get

def setup():
    shelltools.system("qmake6-qt6 PREFIX=/usr LIBDIR=/usr/lib")
    # qt6.configure()

def build():
    # shelltools.cd("build")
    shelltools.system("make")

def install():
    # qt6.install()
    shelltools.system("make INSTALL_ROOT=%s install" % get.installDIR())

    pisitools.dodoc("COPYING", "TODO", "README*")
