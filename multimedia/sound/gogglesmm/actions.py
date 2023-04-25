#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DWITH_ALSA=ON',
    ' -DWITH_CFOX=OFF',
    ' -DWITH_NATIVE=OFF',
    ' -B_build -L '
    ])

def setup():
	#shelltools.unlinkDir("cfox")
	cmaketools.configure(j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS", "../ChangeLog")
