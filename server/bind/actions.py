#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#~ WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-").upper())

BINDDIR="/var/named"
CHROOT="%s/chroot" % BINDDIR

shelltools.export("CPPFLAGS", "%s -DDIG_SIGCHASE" % get.CXXFLAGS())

def setup():
    shelltools.makedirs("m4")
    # Fix PATHs in manpages
    # pisitools.dosed("bin/named/named.8", "/etc/named.conf", "/etc/bind/named.conf")
    # pisitools.dosed("bin/check/named-checkconf.8", "/etc/named.conf", "/etc/bind/named.conf")
    # pisitools.dosed("bin/rndc/rndc.8", "/etc/rndc.conf", "/etc/bind/rndc.conf")
    # pisitools.dosed("bin/rndc/rndc.8", "/etc/rndc.key", "/etc/bind/rndc.key")

    # Adjust version
    # pisitools.dosed("version", "^RELEASEVER=.*$", "RELEASEVER=Pisi Linux-1.0")

    libtools.libtoolize("-cf")
    autotools.aclocal("-I m4")
    autotools.autoreconf("-vfi")

    autotools.configure("--localstatedir=/var \
                         --sysconfdir=/etc/bind \
                         --with-openssl \
                         --with-pic \
                         --enable-linux-caps \
                         --includedir=/usr/include/bind9 \
                         --enable-largefile \
                         --disable-static \
                         --with-randomdev=/dev/urandom \
                         --with-libtool \
                         --enable-threads \
                         --enable-ipv6 \
                         --with-maxminddb \
                         --with-tuning=large \
                         --enable-fixed-rrset \
                         --enable-full-report \
                         --with-python=/usr/bin/python3 \
                         NAMED_CONF=/etc/bind/named.conf \
                         DRNDC_CONFFILE=/etc/bind/rndc.conf \
                         DRNDC_KEYFILE=/etc/bind/rndc.key \
                         PYTHON=/usr/bin/python3")


    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # pisitools.insinto("/etc/bind", "bin/tests/system/common/rndc.key")

    # Prepare chroot jail
    for d in ("dev", "etc/bind", "etc/pki/dnssec-keys", "lib/bind", "var/tmp", "var/log", "var/run/named", "var/named", "etc/bind/rndc.key"):
        pisitools.dodir("%s/%s" % (CHROOT, d))

    # At least drop a file in it
    shelltools.echo("%s%s/README" % (get.installDIR(), CHROOT), "Chroot jail for named")

    # Create directories
    pisitools.dodir("/var/run/named")
    for d in ("pri", "sec", "slaves", "data", "dynamic"):
        pisitools.dodir("%s/%s" % (BINDDIR, d))

    # Create symlinks
    for src, dest in [("named.ca", "%s/root.cache" % BINDDIR),
                      ("%s/pri" % BINDDIR, "/etc/bind/pri"),
                      ("%s/sec" % BINDDIR, "/etc/bind/sec")]:
        pisitools.dosym(src, dest)

    # Documentation
    pisitools.dodoc("CHANGES", "COPYRIGHT", "README*")
    # pisitools.dodoc("doc/misc/*", "contrib/scripts/named-bootconf.sh", "contrib/scripts/nanny.pl")
    pisitools.dohtml("doc/arm/*")
    # pisitools.remove("/usr/share/doc/%s/Makefile*" % get.srcNAME())
