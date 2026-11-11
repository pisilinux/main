#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("""sed -i "s|Eigen3 3.3|Eigen3|g" CMakeLists.txt""")
    shelltools.system("""sed -i "s|Eigen3 \${CERES_EIGEN_VERSION}|Eigen3|g" cmake/CeresConfig.cmake.in""")
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    cmaketools.configure("-Bbuild \
                            -GNinja \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DEIGENSPARSE=ON \
                            -DBUILD_SHARED_LIBS=ON \
                            -DBUILD_TESTING=OFF \
                            -DBUILD_EXAMPLES=OFF \
                            -DBUILD_BENCHMARKS=OFF")

def build():
    shelltools.system("ninja -C build")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("LICENSE", "README*")
