#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	pass

def build():
	pass

def install():
	shelltools.system("make prefix=/usr DESTDIR=%s install" % get.installDIR())

