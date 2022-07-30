#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = '-DCMAKE_BUILD_TYPE=Release -DGUI=QT5 -L '

def setup():
	pisitools.dosed("crengine/include/cr3version.h", "58", "59")
	pisitools.dosed("crengine/include/cr3version.h", "06-13", "08-31")
	cmaketools.configure("-B_build %s" % j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

