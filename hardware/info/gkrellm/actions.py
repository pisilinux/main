#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = ''.join([
    ' without-gnutls=no',
    ' without-ssl=yes',
    ' without-ntlm=yes',
    ' without-libsensors=yes',
    ' INSTALLROOT=/usr',
    ' INCLUDEDIR=/usr/include/gkrellm2',
    ' CFLAGS=\'%s\'' % get.CFLAGS(),
    ' LDFLAGS=\'%s\' ' % get.LDFLAGS()
    ])

def build():
    autotools.make(i)

def install():
    a = get.installDIR()
    b = "DESTDIR=%s PREFIX=/usr CFGDIR=%s/etc" % (a, a)
    autotools.rawInstall(b)

    pisitools.dodoc("CREDITS", "COPYRIGHT", "COPYING")
    pisitools.removeDir("/usr/lib/systemd")
