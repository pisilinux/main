#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("DgRPC_INSTALL=ON \
        -DgRPC_ABSL_PROVIDER=package \
        -DgRPC_BACKWARDS_COMPATIBILITY_MODE=OFF \
        -DgRPC_CARES_PROVIDER=package \
        -DgRPC_PROTOBUF_PROVIDER=package \
        -DgRPC_RE2_PROVIDER=package \
        -DgRPC_SSL_PROVIDER=package \
        -DgRPC_ZLIB_PROVIDER=package \
        -DgRPC_BUILD_TESTS=$(usex test) \
        -DCMAKE_CXX_STANDARD=17", sourceDir="..")

def build():
    cmaketools.make("-C build")

def install():
    shelltools.cd("build")
    cmaketools.install()
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("LICENSE", "README.md")
