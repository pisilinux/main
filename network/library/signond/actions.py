#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import qt6
from pisi.actionsapi import get


def setup():
    shelltools.system("qmake6-qt6 PREFIX=/usr LIBDIR=lib")
    # qt6.configure()

def build():
    autotools.make()
    # qt6.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    # qt6.install()

    pisitools.dodoc("COPYING", "TODO", "README*")
