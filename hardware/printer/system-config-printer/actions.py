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
    #notify-0.8
    #pisitools.dosed("applet.py", "'0.7'", "'0.8'")
    #pisitools.dosed("jobviewer.py", "'0.7'", "'0.8'")

    # we are using different paths
    pisitools.dosed("cupshelpers/cupshelpers.py", "\/lib64\/", "\/lib\/")
    pisitools.dosed("troubleshoot/CheckUSBPermissions.py", "\/usr\/bin\/getfacl", "\/bin\/getfacl")

    pisitools.dosed("Makefile.am", "xmlto man", "xmlto --skip-validation man")
    for i in ["README", "ChangeLog"]:
        shelltools.touch(i)
    #autotools.autoreconf("-fi")
    shelltools.system("./bootstrap")
    autotools.configure("--with-udev-rules \
                         --with-systemdsystemunitdir=no \
                         --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s udevrulesdir=/lib/udev/rules.d udevhelperdir=/lib/udev" % get.installDIR())

    pisitools.insinto("/usr/lib/python3.9/site-packages/cupshelpers", "build/lib/cupshelpers/*.py")

    pisitools.dodir("/run/udev-configure-printer")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "COPYING", "ChangeLog")
