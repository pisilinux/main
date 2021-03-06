#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt5

def setup():
    shelltools.cd("Kvantum")
    qt5.configure()

def build():
    shelltools.cd("Kvantum")
    qt5.make()

def install():
    shelltools.cd("Kvantum")
    qt5.install()

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README*")
