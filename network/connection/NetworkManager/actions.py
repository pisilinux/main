#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    # /var/run => /run
    #for f in ["configure.ac", "src/Makefile.am", "src/Makefile.in"]:
        #pisitools.dosed(f, "\$\(?localstatedir\)?(\/run\/(\$PACKAGE|NetworkManager))", "\\1")
    #pisitools.dosed("configure.ac", "\/var(\/run\/ConsoleKit)", "\\1")
    #pisitools.dosed("configure.ac", "^initscript", deleteLine=True)
    
    shelltools.system("grep -rl '^#!.*python$' | xargs sed -i '1s/python/&3/'")
    pisitools.cxxflags.add("-O2 -fPIC")
    autotools.autoreconf("-fiv")
    shelltools.system("intltoolize --force --copy --automake")

    autotools.configure("--disable-static \
                         --disable-silent-rules \
                         --disable-lto \
                         --disable-config-plugin-ibft \
                         --disable-ifnet \
                         --disable-more-warnings \
                         --enable-wifi \
                         --enable-modify-system \
                         --enable-ppp=yes \
                         --enable-bluez5-dun \
                         --enable-concheck \
                         --without-netconfig \
                         --with-modem-manager-1 \
                         --with-session-tracking=consolekit \
                         --with-suspend-resume=upower \
                         --with-system-ca-path=/etc/ssl/certs \
                         --with-crypto=nss \
                         --with-dhcpcd=/usr/bin/dhcpcd \
                         --with-pppd=/usr/sbin/pppd \
                         --with-pppd-plugin-dir=/usr/lib/pppd/2.4.7 \
                         --with-dbus-sys-dir=/etc/dbus-1/system.d \
                         --with-dhclient=/usr/sbin/dhclient \
                         --with-kernel-firmware-dir=/lib/firmware \
                         --with-udev-dir=/lib/udev \
                         --with-resolvconf=/etc/resolv.default.conf \
                         --with-iptables=/sbin/iptables \
                         --with-dnsmasq=/usr/sbin/dnsmasq \
                         --with-systemdsystemunitdir=no \
                         --with-nmtui \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/NetworkManager \
                        ")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #autotools.make("-k check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/NetworkManager/VPN")

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING", "COPYING", "NEWS", "README")
