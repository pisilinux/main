#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sbindir=/usr/sbin --with-libmount --without-selinux --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s sbindir=/usr/sbin" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
