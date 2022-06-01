#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's@systemd@elogind@' data/pam-lfs/gdm-launch-environment.pam")
    shelltools.system("sed -i 's@-session@session @' data/pam-lfs/gdm-launch-environment.pam")
    shelltools.system("sed -i 's@uid >= 1000@uid >= 0@g' data/pam-lfs/*.pam")

    mesontools.configure("--prefix=/usr \
                          --localstatedir=/var \
                          --buildtype=release \
                          -Ddefault-pam-config=lfs \
                          -Dplymouth=disabled \
                          -Dpam-mod-dir=/lib/security \
                          -Dgdm-xsession=true \
                          -Dsystemd-journal=false \
                          -Dsystemdsystemunitdir=no \
                          -Dsystemduserunitdir=no \
                          -Dlogind-provider=elogind \
                          -Dscreenshot-dir=/var/lib/gdm/greeter")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("NEWS", "README.md", "COPYING", "AUTHORS", "HACKING")
