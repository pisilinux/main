#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, mesontools, pisitools

def setup():
    i = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_BUILD_TYPE=None',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -Bbuild -G Ninja -L '
    ])
    cmaketools.configure(i, sourceDir = "c")
    shelltools.cd("b3sum")
    shelltools.system("cargo fetch --locked")

def build():
    mesontools.build()
    shelltools.cd("b3sum")
    shelltools.system("cargo build --release") # passed with --ignore-sandbox

def install():
    mesontools.install()

    pisitools.dobin("b3sum/target/release/b3sum")

    for l in ["A2", "A2LLVM", "CC0"]:
        pisitools.dodoc("LICENSE_%s" % l)
