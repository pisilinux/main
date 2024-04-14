#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    pisitools.dosed("src/dotconf.c", "dotconf_continue_line_new", "dotconf_continue_line")
    shelltools.system("sed -i 's|cp1, tmp|cp1|g' src/dotconf.c")
    autotools.autoreconf("-i")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README")

