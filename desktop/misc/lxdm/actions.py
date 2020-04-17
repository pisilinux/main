#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
def setup():
    #shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr     \
                         --sysconfdir=/etc \
                         --with-pam        \
                         --enable-gtk3")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install Pisi Linux default theme
    pisitools.dodir("/usr/share/lxdm/themes/lxdm-pisilinux-theme")
    pisitools.insinto("/usr/share/lxdm/themes/lxdm-pisilinux-theme", "lxdm-pisilinux-theme-0.1/*")
    #pisitools.remove("/usr/share/lxdm/themes/lxdm-pisilinux-theme/login.png")
    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "README", "ChangeLog", "NEWS")
