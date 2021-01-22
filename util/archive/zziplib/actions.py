#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j5", "-j1"))

j = ''.join([
    '-DCMAKE_BUILD_TYPE=Release ',
    '-DCMAKE_INSTALL_LIBDIR=lib ',
    ])

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure("%s -G Ninja -L" % j, sourceDir = '..')

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("ChangeLog", "COPYING.LIB", "README", "TODO", "docs/COPYING*", "docs/README.SDL")

