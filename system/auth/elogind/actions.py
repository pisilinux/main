#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("-Drootlibdir=/usr/lib \
                          --prefix=/usr \
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