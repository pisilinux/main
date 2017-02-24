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
    autotools.autoreconf("-fiv")
    shelltools.system("intltoolize --force --copy --automake")

    autotools.configure("--disable-static \
                         --disable-silent-rules \
                         --disable-wimax \
                         --disable-ifcfg-rh \
                         --disable-ifcfg-suse \
                         --disable-ifnet \
                         --disable-ifupdown \
                         --disable-lto \
                         --disable-more-warnings \
                         --enable-introspection \
                         --enable-wifi \
                         --enable-modify-system \
                         --enable-ppp=yes \
                         --enable-bluez5-dun \
                         --enable-concheck \
                         --enable-config-plugin-ibft \
                         --enable-vala=yes \
                         --enable-json-validation \
                         --enable-polkit \
                         --enable-polkit-agent \
                         --without-netconfig \
                         --with-modem-manager-1 \
                         --with-libsoup=yes \
                         --with-session-tracking=consolekit \
                         --with-suspend-resume=upower \
                         --with-system-ca-path=/etc/ssl/certs \
                         --with-crypto=nss \
                         --with-config-dhcp-default=/usr/bin/dhcpcd \
                         --with-pppd=/usr/sbin/pppd \
                         --with-dbus-sys-dir=/etc/dbus-1/system.d \
                         --with-kernel-firmware-dir=/lib/firmware \
                         --with-udev-dir=/lib/udev \
                         --with-resolvconf=/etc/resolv.default.conf \
                         --with-iptables=/usr/sbin/iptables \
                         --with-systemdsystemunitdir=no \
                         --with-nmtui \
                         --with-pppd-plugin-dir=/usr/lib/pppd/2.4.7 \
                         --without-valgrind \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/NetworkManager \
                         --with-dhcpcd=/usr/bin/dhcpcd \
                         --without-dhclient \
                        " )

    pisitools.dosed("libtool", "-shared", "-Wl, --as-needed -shared")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/NetworkManager/VPN")

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING", "COPYING", "NEWS", "README")
