#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    #shelltools.export("MOC5", "moc-qt5")
    shelltools.system("sed -i s/systemd/elogind/ data/pam/*")

    autotools.configure("--prefix=/usr \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --sbindir=/usr/bin \
                         --libexecdir=/usr/lib/lightdm \
                         --disable-static \
                         --disable-tests \
                         --enable-liblightdm-qt5 \
                         --with-greeter-user=lightdm \
                         --with-greeter-session=pisi-lightdm-greeter")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.system("cp tests/src/lightdm-session " + get.installDIR() + "/usr/bin")
    shelltools.system("sed -i '1 s/sh/bash --login/' " + get.installDIR() + "/usr/bin/lightdm-session")

    pisitools.removeDir("/etc/init")
    pisitools.remove("/usr/lib/liblightdm-gobject-1.la")