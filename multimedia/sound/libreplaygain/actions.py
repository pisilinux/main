#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

#from pisi.actionsapi import shelltools
#from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

j = "-DCMAKE_INSTALL_PREFIX=/usr \
     -DCMAKE_BUILD_TYPE=Release \
    "

def setup():
#	cmaketools.configure(j)
	autotools.autoreconf("-fiv")
	autotools.configure("--disable-static")

def build():
#	cmaketools.make()
	autotools.make()

def check():
	pass

def install():
#	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
#	cmaketools.install()

#	shelltools.cd("include")
#	pisitools.insinto("/usr/include", "replaygain")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

