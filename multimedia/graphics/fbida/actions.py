#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

#from pisi.actionsapi import mesontools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "-Wno-strict-prototypes \
     -Wno-missing-prototypes \
     -Wno-unused-result \
     -Wno-format-overflow \
     -Wno-format-truncation \
    "

def build():
	pisitools.dosed("GNUmakefile", "-Wno-pointer-sign", "-Wno-pointer-sign %s" % i)
	autotools.make("prefix=/usr")

def install():
	autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())

	pisitools.dodoc("COPYING", "README", "TODO")

