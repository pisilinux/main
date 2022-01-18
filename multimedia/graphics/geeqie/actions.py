#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
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
	# Fix instalation step
	pisitools.dosed("Makefile.am", "\ ChangeLog\ ", " ")
	pisitools.dosed("Makefile.am", "\ ChangeLog.html$", "")
	# Fix version
	pisitools.dosed("configure.ac", "\+git", "1.7.1")


	autotools.autoreconf("-vif")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.removeDir("/usr/share/doc/")
	pisitools.dodoc("AUTHORS", "NEWS")
