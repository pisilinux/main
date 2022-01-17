#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.system("sed -i -e '/AM_PATH_AALIB,/s/AM_PATH_AALIB/[&]/' aalib.m4")
    autotools.autoreconf("-vfi")

    autotools.configure("--with-slang-driver --with-x11-driver --disable-static")

def build():
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*", "COPYING", "ANNOUNCE")

