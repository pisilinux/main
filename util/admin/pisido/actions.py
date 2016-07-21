#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

WorkDir="PisiDo-2.3.1/pisido"
def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("LICENSE", "LISANS", "OKUBUNU", "README")



# By PiSiDo 2.2.1

# By PiSiDo 2.3.0

# By PiSiDo 2.3.1
