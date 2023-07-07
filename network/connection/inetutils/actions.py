#!/usr/bin/python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    #autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr \
        --libexecdir=/usr/lib \
        --with-systemdsystemunitdir=no \
        --localstatedir=/var \
        --sysconfdir=/etc \
        --with-pam \
        --with-socket-dir=/var/run/inetutils \
        --with-xinetd=/etc/xinetd.d \
        --enable-ftp \
        --enable-ftpd \
        --enable-telnet \
        --enable-telnetd \
        --enable-talk \
        --enable-talkd \
        --disable-rcp \
        --disable-servers \
        --disable-rlogin \
        --disable-rsh \
        --disable-rexec \
        --disable-rexecd \
        --disable-tftp \
        --disable-tftpd \
        --disable-ping \
        --disable-ping6 \
        --disable-logger \
        --disable-syslogd \
        --disable-inetd \
        --disable-whois \
        --disable-uucpd \
        --disable-ifconfig \
        --disable-traceroute")

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "README")
