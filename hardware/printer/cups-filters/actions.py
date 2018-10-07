# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("configure", "localstatedir/run/cups", "localstatedir/cups")
    #shelltools.system("./autogen.sh")
    autotools.configure("--sbindir=/usr/bin \
                         --localstatedir=/var \
                         --enable-dbus \
                         --with-rcdir=no \
                         --disable-mutool \
                         --disable-static \
                         --with-gs-path=/usr/bin/gs \
                         --with-pdftops-path=/usr/bin/gs \
                         --docdir=/usr/share/doc/cups-filters-1.0.76 \
                         --with-browseremoteprotocols=DNSSD,CUPS ")
                         #--with-test-font-path=/usr/share/fonts/TTF/DejaVuSans.ttf")

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("check")

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
