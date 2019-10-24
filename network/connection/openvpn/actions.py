#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	# First build OpenSSL. OpenVPN requires OpenSSL => 1.1.0, but we cannot provide it at the moment.
	# We build OpenSSL statically for OpenVPN
	shelltools.system("echo -e '\033[0;36mBuilding OpenSSL\033[0m' ")
	shelltools.cd("openssl-1.1.1d")
	shelltools.system("./Configure --prefix=%s/openssl --openssldir=%s/openssl/etc/ssl --libdir=lib no-shared enable-ec_nistp_64_gcc_128 linux-x86_64 -Wa,--noexecstack" %(get.workDIR(), get.workDIR()))
	autotools.make()
	autotools.make("install")

	# Now we can build OpenVPN
	shelltools.system("echo -e '\033[0;36mBuilding OpenVPN\033[0m' ")
	shelltools.export("CFLAGS", "-I%s/openssl/include -O3" %get.workDIR())
	shelltools.export("LDFLAGS", "-L%s/openssl/lib -lssl -lcrypto -lpthread -ldl" %get.workDIR())
	shelltools.cd("..")
	autotools.autoreconf("-vfi")
	autotools.configure("--enable-pthread \
						 --enable-password-save \
                         --enable-iproute2 \
                         --enable-pkcs11 \
                         --enable-plugins \
                         --enable-crypto \
                         --with-ifconfig-path=/sbin/ifconfig \
                         --with-iproute-path=/sbin/ip \
                         --with-route-path=/sbin/route \
                         OPENSSL_CFLAGS='-I%s/openssl/include -O3' \
                         OPENSSL_LIBS='-L%s/openssl/lib -lssl -lcrypto -lpthread -dl' \
                         " % (get.workDIR(), get.workDIR()))

def build():
    autotools.make()


def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/openvpn")
     
    pisitools.dodoc("AUTHORS", "COPYING", "COPYRIGHT.GPL", "Changes.rst", "README*")

