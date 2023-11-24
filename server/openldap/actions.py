#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial = ["libtool"]

def setup():
    pisitools.dosed(
        "include/ldap_defaults.h",
        "(#define LDAPI_SOCK).*",
        '\\1 "/run/openldap/slapd.sock"'
    )
    pisitools.dosed("servers/slapd/Makefile.in", "(\$\(DESTDIR\))\$\(localstatedir\)(\/run)", r"\1\2")

    # pisitools.flags.add("-D_REENTRANT -D_GNU_SOURCE -fPIC -Wl,--as-needed -DLDAP_CONNECTIONLESS")

    # shelltools.system("sed -i 's|%LOCALSTATEDIR%/run|/run/openldap|' servers/slapd/slapd.{conf,ldif}")
    shelltools.system("sed -i 's|-m 644 $(LIBRARY)|-m 755 $(LIBRARY)|' libraries/{liblber,libldap}/Makefile.in")
    #pisitools.ldflags.add("-pie")

    options = "--prefix=/usr \
               --enable-backends=mod \
               --enable-slapd \
               --enable-passwd=mod \
               --enable-dnssrv=mod \
               --enable-ldap \
               --enable-meta=mod \
               --enable-null=mod \
               --enable-rlookups \
               --enable-modules \
               --enable-cleartext \
               --enable-slapi \
               --enable-dyngroup \
               --enable-proxycache \
               --enable-syslog \
               --enable-dynamic \
               --enable-local \
               --enable-overlays=mod \
               --with-pic \
               --without-fetch \
               --disable-wt \
               --enable-crypt \
               --enable-ipv6 \
               --enable-dynacl \
               --enable-shared \
               --enable-static=no \
               --disable-slp \
               --localstatedir=/var/lib"
                              # --enable-aci \
                            # --enable-wrappers \

    if get.buildTYPE() == "emul32":
        options +=  " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --libexecdir=/usr/lib32 \
                     --disable-bdb \
                     --disable-hdb \
                     --disable-wrappers \
                     --disable-spasswd \
                     --disable-perl \
                     --with-tls=auto \
                     --disable-ndb \
                     --disable-sql \
                     --without-cyrus-sasl"

    else: options += " --enable-wrappers \
                                  --enable-spasswd \
                                  --enable-perl \
                                  --libdir=/usr/lib \
                                  --libexecdir=/usr/lib \
                                  --enable-mdb=yes \
                                  --with-cyrus-sasl \
                                  --enable-bdb=yes \
                                  --enable-hdb=yes \
                                  --with-gnu-ld \
                                  --with-threads \
                                  --with-tls=auto"

    shelltools.export("AUTOMAKE", "/bin/true")
    autotools.autoreconf("-fi")
    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        pisitools.dosym("/usr/lib/libslapi.so.2.0.200", "/usr/lib/libldap-2.4.so.2")
        pisitools.dosym("/usr/lib/liblber.so.2.0.200", "/usr/lib/liblber-2.4.so.2")
        pisitools.dosym("/usr/lib/libslapi.so.2.0.200", "/usr/lib/libslapi-2.4.so.2")
        # pisitools.dosym("/usr/lib/slapd", "/usr/libexec/slapd")
        pisitools.dosym("/usr/lib/slapd", "/usr/bin/slapd")
        pisitools.remove("/usr/lib32/*.la")
        pisitools.remove("/usr/lib32/openldap/*.la")
        return

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.dodir("/run/openldap")
    pisitools.dodir("/etc/openldap/ssl")

    pisitools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYRIGHT", "README", "LICENSE")

    pisitools.remove("/usr/lib/*.la")
    pisitools.remove("/usr/lib/openldap/*.la")
