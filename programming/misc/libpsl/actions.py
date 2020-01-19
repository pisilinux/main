#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-gtk-doc \
                         --enable-runtime=libicu \
                         --enable-builtin=libicu")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/libpsl", "effective_tld_names.dat")
    pisitools.insinto("/usr/share/libpsl", "test_psl.txt")

    pisitools.dodoc("AUTHORS", "COPYING", "README*", "LICENSE")
