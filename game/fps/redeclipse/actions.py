#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "redeclipse-%s" % get.srcVERSION()

def build():
	#shelltools.system("rm -rf data/*")
	#shelltools.system("cp -r redeclipse-%s/data/*", "data")
    
	shelltools.cd("src")
	autotools.make("client server")

def install():
	shelltools.cd("src")
	autotools.rawInstall("DESTDIR=%s prefix=/usr system-install" % get.installDIR())	

	shelltools.cd("..")
	pisitools.dodoc("doc/*.txt", "readme.txt")
