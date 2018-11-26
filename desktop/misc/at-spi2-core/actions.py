#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "meson --prefix=/usr --sysconfdir=/etc --libexec=/usr/libexec/at-spi2 \
                     -D enable_docs=true \
              "
    
    if get.buildTYPE() == "emul32":
        options += "--prefix=/usr --libdir=lib32 -D enable_docs=false .."
        
        
    shelltools.system(options)
    
def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    
def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        #pisitools.dosed("%s/usr/share/dbus-1/services" % get.installDIR(), "^(Exec=)\/usr/tmp", r"\1/usr/libexec/at-spi2")
        #pisitools.dosed("%s/usr/share/dbus-1/accessibility-services" % get.installDIR(), "^(Exec=)\/usr/tmp", r"\1/usr/libexec/at-spi2")
        #pisitools.dosed("%s/etc/dbus-1/system.d" % get.installDIR(), "^(ExecStart=)\/usr/tmp", r"\1/usr/libexec/at-spi2")
        #pisitools.removeDir("/usr/tmp")
        return
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "NEWS", "README")

