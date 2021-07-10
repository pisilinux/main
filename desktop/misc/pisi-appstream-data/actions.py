#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def install():
    shelltools.system("DESTDIR=%s appstream-util install pisi-1.xml.gz pisi-1-icons.tar.gz" % get.installDIR())
    shelltools.system("chmod 00755 %s/usr/share/app-info/xmls" % get.installDIR())
    shelltools.system("chmod 00644 %s/usr/share/app-info/xmls/pisi-1.xml.gz" % get.installDIR())
    shelltools.system("ln -sv pisi-1 '%s/usr/share/app-info/icons/pisi'" % get.installDIR())
