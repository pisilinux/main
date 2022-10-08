#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt6
from pisi.actionsapi import pisitools


def setup():
    qt6.configure()

def build():
    qt6.make()

def install():
    qt6.install()


    pisitools.dodoc("LICENSES/*")
