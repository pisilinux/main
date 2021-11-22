#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.touch("ChangeLog")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
              --sbindir=/usr/bin \
              --sysconfdir=/etc \
              --with-drivedbdir \
              --with-libsystemd=no \
              --with-libcap-ng=yes \
              --with-smartdscriptdir=/usr/share/smartmontools \
              --with-smartdplugindir=/usr/share/smartmontools/smartd_warning.d \
            --with-systemdsystemunitdir=no")

def build():
    autotools.make("CXXFLAGS='%s -fpie'" % get.CXXFLAGS())

def install():
    pisitools.dosed("smartd.service.in","sysconfig/smartmontools","conf.d/smartd")
    pisitools.dosed("smartd.service.in","smartd_opts","SMARTD_ARGS")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README", "smartd.conf")
