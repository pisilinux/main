#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    #autotools.autoreconf('-fi')
    autotools.configure("--enable-gtk2 --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()


def install():
    autotools.install()

    # Empty files: NEWS,
    pisitools.dodoc("COPYING", "README", "AUTHORS", "ChangeLog")
