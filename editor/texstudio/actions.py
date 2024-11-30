#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6

j = "USE_SYSTEM_QUAZIP=1 USE_SYSTEM_HUNSPELL=1 INTERNAL_TERMINAL=1 \
	  QUAZIP_LIB=-lquazip1-qt6 \
	  QUAZIP_INCLUDE='/usr/include/QuaZip-Qt6-1.4/quazip'"

def setup():
	#qt6.configure("texstudio.pro", parameters='%s' % j)
	qt6.configure()

def build():
	qt6.make()

def install():
	qt6.install()

	pisitools.dodoc("README.md")

