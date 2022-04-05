#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

j = "USE_SYSTEM_QUAZIP=1 USE_SYSTEM_HUNSPELL=1 INTERNAL_TERMINAL=1"

def setup():
	qt5.configure("texstudio.pro", parameters='%s' % j)

def build():
	qt5.make()

def install():
	qt5.install()

#	pisitools.dodoc("COPYING", "README.md")

