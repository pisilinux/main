#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "DDNet-%s" % get.srcVERSION()

def setup():
    shelltools.system(
        "cmake -S . -B build -G Ninja "
        "-DCMAKE_INSTALL_PREFIX=/usr "
        "-DCMAKE_BUILD_TYPE=None "
        "-DAUTOUPDATE=OFF "
        "-DDISCORD=OFF "
        "-DDISCORD_DYNAMIC=OFF "
        "-DVIDEORECORDER=ON "
        "-DUPNP=ON "
        "-DMYSQL=ON "
        "-DTEST_MYSQL=OFF "
        "-DPREFER_BUNDLED_LIBS=OFF"
    )

def build():
    shelltools.system("ninja -C build")

def install():
    pisitools.dosed(
        "data/autoexec_server.cfg",
        "sv_test_cmds 1",
        "sv_test_cmds 0"
    )

    pisitools.dosed(
        "data/autoexec_server.cfg",
        "myServerconfig.cfg",
        "autoexec_server_maps.cfg"
    )

    shelltools.system(
        "DESTDIR=%s ninja -C build install" % get.installDIR()
    )

    pisitools.dodoc("license.txt", "README.md")