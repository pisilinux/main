#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools, qt5, get

WorkDir = "Kvantum-%s/Kvantum" % get.srcVERSION()

def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("ChangeLog")
