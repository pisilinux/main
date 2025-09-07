#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson --libexecdir=/usr/lib \
        --prefix=/usr \
        -Drunstatedir=/run \
        -Dqemu_user=libvirt-qemu \
        -Dqemu_group=libvirt-qemu \
        -Dnetcf=disabled \
        -Dopenwsman=disabled \
        -Dapparmor=disabled \
        -Dapparmor_profiles=disabled \
        -Dselinux=disabled \
        -Dwireshark_dissector=disabled \
        -Ddriver_bhyve=disabled \
        -Ddriver_hyperv=disabled \
        -Ddriver_libxl=disabled \
        -Ddriver_vz=disabled \
        -Dsanlock=disabled \
        -Dsecdriver_apparmor=disabled \
        -Dsecdriver_selinux=disabled \
        -Dstorage_sheepdog=disabled \
        -Dstorage_vstorage=disabled \
        -Ddtrace=disabled \
        -Dnumad=disabled \
        -Dstorage_zfs=enabled \
        -Ddocs=disabled ..")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("COPYING*", "NEWS*", "README*")
