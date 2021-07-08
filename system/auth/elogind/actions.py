#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    mesontools.configure("--prefix=/usr \
                          -Drootlibdir=/usr/lib \
                          -Dpolkit=true \
                          -Dsplit-bin=true \
                          -Dsplit-usr=false \
                          -Dhalt-path=/sbin/halt \
                          -Dpamlibdir=/lib/security \
                          -Dreboot-path=/sbin/reboot \
                          -Dcgroup-controller=elogind \
                          -Ddefault-hierarchy=unified \
                          -Dpoweroff-path=/sbin/poweroff \
                          -Ddocdir=/usr/share/doc/elogind \
                          -Drootlibexecdir=/usr/lib/elogind \
                          -Ddefault-kill-user-processes=false \
                          -Ddbuspolicydir=/usr/share/dbus-1/system.d")

def build():
    mesontools.build()

def install():
    mesontools.install()

    shelltools.system("ln -s libelogind.pc %s/usr/lib/pkgconfig/libsystemd.pc" % get.installDIR())
    shelltools.system("ln -s libelogind.pc %s/usr/lib/pkgconfig/libsystemd-logind.pc" % get.installDIR())
    shelltools.system("ln -sr %s/usr/include/elogind %s/usr/include/systemd" % (get.installDIR(), get.installDIR()))