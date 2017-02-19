#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools



def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()


    pisitools.dodoc("LICENSE.FDL", "LICENSE.GPLv2", "LICENSE.GPLv3", "LICENSE.LGPLv3")

