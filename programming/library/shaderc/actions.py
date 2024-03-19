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
    # shelltools.system("python3 ./utils/git-sync-deps")
    shelltools.system("sed '/examples/d;/third_party/d' -i CMakeLists.txt")

    shelltools.system("sed '/build-version/d' -i glslc/CMakeLists.txt")


    cmaketools.configure("-B build \
                             -GNinja \
                            -DCMAKE_BUILD_TYPE=Release \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DSHADERC_SKIP_TESTS=ON \
                            -Dglslang_SOURCE_DIR=/usr/include/glslang \
                            -DPYTHON_EXECUTABLE=python3")

def build():
    shelltools.system("ninja -C build")

def install():
    shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

    # pisitools.removeDir("/usr/include/spirv-tools")
    # pisitools.removeDir("/usr/lib/cmake")
    # pisitools.remove("/usr/lib/libSPIRV-Tools*")
    # pisitools.remove("/usr/lib/pkgconfig/SPIRV*")
    # pisitools.remove("/usr/bin/spirv*")

    pisitools.dodoc("AUTHORS", "LICENSE", "CONTRIBUTORS*", "README*")
