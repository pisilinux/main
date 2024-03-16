#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt6, get

def setup():
    shelltools.system("sed -i '/-Werror/d' common-project-config.pri")
    pisitools.dosed("common-project-config.pri", "lib64", "lib")
    # qt6.configure
    shelltools.system("qmake6-qt6 PREFIX=/usr LIBDIR=/usr/lib")

def build():
    # qt6.make("PREFIX=/usr LIBDIR=/usr/lib")
    shelltools.system("make")

def install():
    # qt6.install()
    shelltools.system("make INSTALL_ROOT=%s install" % get.installDIR())

    pisitools.dodoc("COPYING", "README*")
