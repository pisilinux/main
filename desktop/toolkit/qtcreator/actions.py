#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    pisitools.dodir("/usr")
    qt5.install()
    pisitools.domove("/share", "/usr")
    pisitools.domove("/lib", "/usr")
    pisitools.domove("/bin", "/usr")
    pisitools.rename("/usr/bin/qtcreator", "qtcreator-bin")
    pisitools.domove("/usr/share/qtcreator/debugger/LGPL_EXCEPTION.TXT", "/usr/share/licenses/qtcreator")
