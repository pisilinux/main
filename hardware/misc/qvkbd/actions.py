#!/usr/bin/python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools

def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("README.md", "COPYING")

