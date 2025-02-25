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
    shelltools.system("sed -i '/Disable polkit/,+8 d' meson.build")
    shelltools.system("""sed '/request_name/i\
                            r = sd_bus_set_exit_on_disconnect(m->bus, true);\
                            if (r < 0)\
                            return log_error_errno(r, "Failed to set exit on disconnect: %m");' \
                            -i src/login/logind.c""")

    mesontools.configure("--prefix=/usr \
                          --libexecdir=/usr/lib/elogind \
                          -Dudevrulesdir=/lib/udev/rules.d \
                          -Dpamconfdir=/etc/pam.d \
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
                          -Ddefault-kill-user-processes=false \
                          -Ddbuspolicydir=/usr/share/dbus-1/system.d")
                              # -Drootlibdir=/usr/lib \
                            # -Drootlibexecdir=/usr/lib/elogind \


def build():
    mesontools.build()

def install():
    mesontools.install()

    shelltools.system("ln -s libelogind.pc %s/usr/lib/pkgconfig/libsystemd.pc" % get.installDIR())
    shelltools.system("ln -s libelogind.pc %s/usr/lib/pkgconfig/libsystemd-logind.pc" % get.installDIR())
    shelltools.system("ln -sr %s/usr/include/elogind %s/usr/include/systemd" % (get.installDIR(), get.installDIR()))
