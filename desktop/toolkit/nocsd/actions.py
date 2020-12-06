#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#def setup():
#	

def build():
	autotools.make("prefix=/usr")

def install():
	autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())

	pisitools.dodoc("ChangeLog", "COPYING", "README.md")
