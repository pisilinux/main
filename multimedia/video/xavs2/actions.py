#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip=["/usr/lib"]

def setup():
	shelltools.cd("build/linux")
	autotools.rawConfigure("--prefix=/usr \
		                    --extra-ldflags='-Wl,-z,noexecstack' \
						    --chroma-format='all' \
							--enable-shared \
						    --enable-lto \
						    --enable-pic \
						    --disable-swscale \
						    --disable-lavf \
						    --disable-ffms \
						    --disable-gpac \
		                    ")

def build():
	shelltools.cd("build/linux")
	autotools.make()

def install():
	shelltools.cd("build/linux")
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())
	pisitools.remove("/usr/lib/libxavs2.a")
	shelltools.cd("../..")
	pisitools.dodoc("COPYING", "README.md")

