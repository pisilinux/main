#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

j = "USE_SYSTEM_QUAZIP=1 USE_SYSTEM_HUNSPELL=1 INTERNAL_TERMINAL=1 \
	  QUAZIP_LIB=-lquazip1-qt5 \
	  QUAZIP_INCLUDE='usr/include/QuaZip-Qt5-1.4/quazip'"

def setup():
	#qt5.configure("texstudio.pro", parameters='%s' % j)
	qt5.configure()

def build():
	qt5.make()

def install():
	qt5.install()

#	pisitools.dodoc("COPYING", "README.md")

