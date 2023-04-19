#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools


def setup():
    # /var/run => /run
    #for f in ["configure.ac", "src/Makefile.am", "src/Makefile.in"]:
        #pisitools.dosed(f, "\$\(?localstatedir\)?(\/run\/(\$PACKAGE|NetworkManager))", "\\1")
    #pisitools.dosed("configure.ac", "\/var(\/run\/ConsoleKit)", "\\1")
    #pisitools.dosed("configure.ac", "^initscript", deleteLine=True)
    
    #shelltools.system("grep -rl '^#!.*python$' | xargs sed -i '1s/python/&3/'")

    #pisitools.dosed("src/core/nm-hostname-manager.c", "/etc/hostname", "/etc/env.d/01hostname")
    pisitools.cxxflags.add("-O2 -fPIC")

    mesontools.configure("-Dmodify_system=true \
                          -Difupdown=false \
                          -Dconfig_plugins_default=keyfile \
                          -Dhostname_persist=default \
                          -Dqt=false \
                          -Dselinux=false \
                          -Debpf=true \
                          -Ddocs=true \
                          -Diwd=true \
                          -Difcfg_rh=true \
                          --buildtype=release \
                          -Dbluez5_dun=true \
                          -Dnetconfig=no \
                          -Dsession_tracking=elogind \
                          -Dsession_tracking_consolekit=false \
                          -Dsuspend_resume=upower \
                          -Dcrypto=nss \
                          -Ddhcpcd=enabled \
                          -Dpppd=/usr/sbin/pppd \
                          -Dpppd_plugin_dir=/usr/lib/pppd/2.4.9 \
                          -Ddbus_conf_dir=/usr/share/dbus-1/system.d \
                          -Ddhclient=enabled \
                          -D config_dns_rc_manager_default=symlink \
                          -Dudev_dir=/lib/udev \
                          -Diptables=/sbin/iptables \
                          -Ddnsmasq=/usr/sbin/dnsmasq \
                          -Dsystemdsystemunitdir=no \
                          -Dsystemd_journal=false \
                          --localstatedir=/var \
                          --sysconfdir=/etc \
                          --libexecdir=/usr/lib/NetworkManager")

def build():
    mesontools.build()

#def check():
    #mesontools.build("test")

def install():
    mesontools.install()

    pisitools.dodir("/etc/NetworkManager/VPN")

    #pisitools.dosym("/etc/env.d/01hostname", "/etc/hostname")

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING*", "COPYING", "NEWS", "README*")
