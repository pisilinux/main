#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr'
    ' -DCMAKE_BUILD_TYPE=None',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DCYTHON_EXECUTABLE=/usr/bin/cython3',
    ' -DWITH_DBUS=OFF',
    ' -DWITH_GSPELL=OFF',
    ' -DWITH_IMAGE_MAGICK=OFF',
    ' -DBUILD_STATIC_LIBS=OFF',
    ' -D2GEOM_BOOST_PYTHON=OFF',
    ' -D2GEOM_CYTHON_BUILD_SHARED=OFF',
    ' -D2GEOM_CYTHON_BINDINGS=OFF',
    ' -DBUILD_TESTING=OFF',
    ' -D2GEOM_PERFOMANCE_TESTS=OFF -L ',
    ])

def setup():
    #fix shebang
#    shelltools.system("find share/extensions -iname '*.py' -exec sed -i 's|env\ python$|env python3|g' {} \;")
    #if with imagemagick build.
#    shelltools.export("PKG_CONFIG_PATH", "${PKG_CONFIG_PATH}:/usr/lib/imagemagick6/pkgconfig")
#    shelltools.export("JOBS", "-j5")
    cmaketools.configure("-B_build %s" % j)

def build():
    shelltools.cd("_build")
    cmaketools.make()

def install():
    shelltools.cd("_build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("../AUTHORS", "../NEWS.md", "../README.md")
