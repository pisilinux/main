#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

j = ''.join([
    ' --disable-map',
    ' --disable-pdf',
    ' --disable-djvu',
    ' --disable-gtk3',
    ' --disable-gpu-accel',
    ' --disable-debug-log '
    ])

def setup():
	pisitools.cflags.add("-Wno-deprecated-declarations")
	shelltools.system("NOCONFIGURE=1 ./autogen.sh")

	autotools.autoreconf("-vif")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "NEWS")
	pisitools.removeDir("/usr/share/doc/geeqie-%s" % get.srcVERSION())
