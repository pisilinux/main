#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' --prefix=/usr',
    ' --with-expat',
    ' --without-{gssapi,libproxy}',
    ' --with-ssl=openssl',
    ' --with-ca-bundle=/etc/pki/tls/certs/ca-bundle.crt',
    ' --enable-threadsafe-ssl=posix',
    ' --enable-shared',
    ' --enable-static=no '
    ])

def setup():
    autotools.configure(i)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/usr/share/doc/neon" % get.installDIR())

    pisitools.dodoc("AUTHORS", "THANKS")
