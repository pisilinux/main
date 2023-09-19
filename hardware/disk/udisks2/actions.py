#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    # Fedora: default to ntfs-3g
    shelltools.system("sed -i data/builtin_mount_options.conf -e 's/ntfs_drivers=ntfs3,ntfs/ntfs_drivers=ntfs,ntfs3/'")
    autotools.configure("--disable-static \
                         --enable-fhs-media \
                         --enable-btrfs \
                         --enable-lvm2 \
                         --with-systemdsystemunitdir=no \
                         --disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")
