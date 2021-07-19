# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/cups-pk-helper")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.system("install -dm755 %s/usr/share/dbus-1/system.d" % get.installDIR())
    pisitools.domove("/etc/dbus-1/system.d/*", "/usr/share/dbus-1/system.d")
    pisitools.removeDir("/etc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "NEWS", "HACKING")
