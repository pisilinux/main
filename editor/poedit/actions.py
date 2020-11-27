#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "-Wno-deprecated-copy \
     -Wno-missing-field-initializers \
     -Wno-cast-function-type \
     -Wno-ignored-qualifiers \
    "
j = "--with-wx-config=wx-config-gtk3 \
     --without-cld2 \
     --without-cpprest \
    "

def setup():
	pisitools.cxxflags.add(i)
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")

