#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# to avoid sandbox violations during make test
shelltools.export("ODBCINI", get.workDIR())
shelltools.export("ODBCSYSINI", get.workDIR())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-apr=/usr \
                         --includedir=/usr/include/apr-1 \
                         --with-ldap \
                         --with-sqlite3 \
                         --with-pgsql \
                         --with-odbc=/usr \
                         --with-mysql \
                         --with-berkeley-db \
                         --with-berkeley-db=/usr \
                         --with-openssl=/usr \
                         --with-sqlite3=/usr \
                         --with-nss=/usr \
                         --with-odbc=/usr \
                         --with-pgsql=/usr \
                         --with-mysql=/usr \
                         --with-oracle=/usr \
                         --without-sqlite2")
    
    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    shelltools.system("make -j1 check")
    # autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosed("%s/usr/bin/apu-1-config" % get.installDIR(), get.workDIR(), "")

    pisitools.dodoc("CHANGES", "NOTICE")
