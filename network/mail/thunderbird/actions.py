#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.insinto("/opt", "*")
    shelltools.system("mkdir -p %s/usr/bin" % get.installDIR())
    shelltools.system("ln -s %s/opt/thunderbird %s/usr/bin/thunderbird" % (get.installDIR(), get.installDIR()))
    for i in ("16", "22", "24", "32", "48", "64", "128", "256"):
        pisitools.dodir("/usr/share/icons/hicolor/%sx%s/apps" % (i, i))
        pisitools.domove("/opt/chrome/icons/default/default%s.png" % (i), "/usr/share/icons/hicolor/%sx%s/apps" % (i, i),"thunderbird.png")
    # Use system certificates
    pisitools.dodir("/usr/lib")
    shelltools.system("ln -s %s/opt/libnssckbi.so %s/usr/lib/libnssckbi.so" % (get.installDIR(), get.installDIR()))
