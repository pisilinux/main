#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

def setup():
    shelltools.system("sed -i '/^documents.*doc/s/ClamAV-GUI/clamav-gui/' clamav-gui.pro")
    shelltools.system("qmake-qt6 PREFIX=/usr clamav-gui.pro")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dodoc("LICENSE")
