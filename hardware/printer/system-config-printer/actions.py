#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # we are using different paths
    pisitools.dosed("cupshelpers/cupshelpers.py", "\/lib64\/", "\/lib\/")
    pisitools.dosed("troubleshoot/CheckUSBPermissions.py", "\/usr\/bin\/getfacl", "\/bin\/getfacl")

    pisitools.dosed("Makefile.am", "xmlto man", "xmlto --skip-validation man")
    for i in ["README", "ChangeLog"]:
        shelltools.touch(i)
    autotools.autoreconf("-fi")
    autotools.configure("--with-udev-rules \
                         --with-systemdsystemunitdir=no \
                         --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s udevrulesdir=/lib/udev/rules.d udevhelperdir=/lib/udev" % get.installDIR())

    pisitools.dodir("/run/udev-configure-printer")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "COPYING", "ChangeLog")
