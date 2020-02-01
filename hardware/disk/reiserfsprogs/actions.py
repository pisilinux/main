#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i '/parse_time.h/i #define _GNU_SOURCE' lib/parse_time.c")
    pisitools.flags.add("-std=gnu89")
    autotools.autoreconf("-fiv")
    autotools.configure("--prefix=/usr --sbindir=/sbin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README")
