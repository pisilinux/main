#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.cd("lcl/interfaces/qt6/cbindings")
    shelltools.system("qmake6-qt6")

def build():
    shelltools.cd("lcl/interfaces/qt6/cbindings")
    autotools.make()

def install():
    shelltools.cd("lcl/interfaces/qt6/cbindings")
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())