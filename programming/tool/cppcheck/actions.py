#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

t = 'FILESDIR=/usr/share/cppcheck CFGDIR=/usr/share/cppcheck/cfg'

def build():
	pisitools.cxxflags.add("-DNDEBUG -Wall -Wno-sign-compare -Wno-unused-function")
	autotools.make("MATCHCOMPILER=yes %s HAVE_RULES=yes" % t)

def check():
	autotools.make("check %s" % t)

def install():
	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), t))

	pisitools.dodoc("AUTHORS", "COPYING", "readme*")

