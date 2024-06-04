#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/freetds/work/ and:
# WorkDir="freetds-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc/freetds \
                         --enable-msdblib \
                         --with-unixodbc=/usr \
                         --with-openssl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING*", "README.md")
