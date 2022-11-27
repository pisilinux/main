#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.export("LDFLAGS", "%s -lz" % get.LDFLAGS())
	perlmodules.configure()

def build():
	perlmodules.make()

def check():
	#perlmodules.make("test")
	pass

def install():
	perlmodules.install()

	pisitools.dodoc("LICENSE", "NEWS", "README")

