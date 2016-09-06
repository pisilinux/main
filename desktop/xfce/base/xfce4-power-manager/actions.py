# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
def setup():
    shelltools.export("GTK3","/usr/bin/gtk-launch")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --sbindir=/usr/bin \
                         --libexecdir=/usr/lib \
                         --localstatedir=/var \
                         --disable-network-manager \
                         --enable-polkit \
                         --disable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
