#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

j = ''.join([
    ' -DWITH_DBUS=ON',
    ' -DBUILD_TESTING=OFF',
    ' -DWITH_GSPELL=OFF',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DWITH_IMAGE_MAGICK=OFF',
    ' -DBUILD_STATIC_LIBS=OFF',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DCYTHON_EXECUTABLE=/usr/bin/cython3',
    ' -D2GEOM_BOOST_PYTHON=ON',
    ' -D2GEOM_CYTHON_BINDINGS=ON',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_PREFIX=/usr -L '
    ])

def setup():
    #fix shebang
#    shelltools.system("find share/extensions -iname '*.py' -exec sed -i 's|env\ python$|env python3|g' {} \;")
    #if with imagemagick build.
#    shelltools.export("PKG_CONFIG_PATH", "${PKG_CONFIG_PATH}:/usr/lib/imagemagick6/pkgconfig")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(j, sourceDir = '..')

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("../AUTHORS", "../NEWS.md", "../README.md")
