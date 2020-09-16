#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

j = "-DBUILD_TESTING=OFF -L \
     -DBUILD_SHARED_LIBS=ON \
     -DWITH_IMAGE_MAGICK=OFF \
     -DBUILD_STATIC_LIBS=OFF \
     -DCMAKE_INSTALL_LIBDIR=lib \
     -DCMAKE_BUILD_TYPE=Release \
     -DCMAKE_INSTALL_PREFIX=/usr \
    "

shelltools.export("PYTHON", "/usr/bin/python3")

def setup():
    # fix shebang
    shelltools.system("find share/extensions -iname '*.py' -exec sed -i 's|env\ python$|env python3|g' {} \;")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(j, sourceDir = '..')

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README.md")