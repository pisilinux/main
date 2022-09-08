#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DPYTHON_EXECUTABLE=/usr/bin/python3',
    ' -DZ3_USE_LIB_GMP=True',
    ' -DZ3_LINK_TIME_OPTIMIZATION=True',
    ' -DZ3_BUILD_LIBZ3_SHARED=True',
    ' -DZ3_BUILD_PYTHON_BINDINGS=True',
    ' -DZ3_INSTALL_PYTHON_BINDINGS=True '
    ])

shelltools.export("PYTHON", "/usr/bin/python3")

def setup():
	cmaketools.configure("-Bbuild %s -G 'Ninja'" % j)

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("RELEASE_NOTES.md")

