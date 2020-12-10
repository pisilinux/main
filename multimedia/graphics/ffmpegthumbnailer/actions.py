#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_BUILD_TYPE=Release \
     -DCMAKE_INSTALL_DIR=/usr \
     -DCMAKE_INSTALL_LIBDIR=lib \
     -DENABLE_THUMBNAILER=ON \
     -DENABLE_GIO=ON \
     -DENABLE_TESTS=OFF \
    "

def setup():
#	pisitools.dosed("libffmpegthumbnailer/pngwriter.cpp", "#include <cassert>", "#include <cassert>\n#include <cstring>")
	pisitools.cxxflags.add("-Wno-deprecated-declarations")
	cmaketools.configure(j)

def build():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README.md")

