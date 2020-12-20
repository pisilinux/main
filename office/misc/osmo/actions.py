#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--enable-backup \
     --enable-printing \
     --with-notes \
     --with-tasks \
     --with-contacts \
    "

def setup():
	pisitools.cflags.add("-Wno-pointer-sign -Wno-unused-result")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FAQ", "README", "TRANSLATORS")

