#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


def setup():
    options = "--prefix=/usr \
                     -Duse_systemd=false \
                     -Ddefault_bus=dbus-daemon \
                     --sysconfdir=/etc \
                     -Dintrospection=enabled \
                     -Ddbus_daemon=/usr/bin/dbus-daemon \
                     -Dsystemd_user_dir=/tmp \
                     --buildtype=release \
                     -D docs=true \
              "
    
    if get.buildTYPE() == "emul32":
        options += " --datadir=/usr/emul32 \
                    --libexec=/usr/lib32/at-spi2 \
                    --sysconfdir=/usr/emul32 \
                    --libdir=lib32 \
                    -Dintrospection=disabled \
                    -D docs=false"

    else:
        options += " --libexec=/usr/lib/at-spi2"

        
    mesontools.configure(options)
    
def build():
    mesontools.build()
    
def install():
    mesontools.install()
    if get.buildTYPE() == "emul32":
        #pisitools.dosed("%s/usr/share/dbus-1/services" % get.installDIR(), "^(Exec=)\/usr/tmp", r"\1/usr/libexec/at-spi2")
        #pisitools.dosed("%s/usr/share/dbus-1/accessibility-services" % get.installDIR(), "^(Exec=)\/usr/tmp", r"\1/usr/libexec/at-spi2")
        # pisitools.dosed("%s/usr/lib/systemd/user" % get.installDIR(), "^(ExecStart=)\/usr/emul32", r"\1/usr/libexec/at-spi2")
        pisitools.removeDir("/usr/emul32")
        # pisitools.removeDir("/tmp")
        # pisitools.dosym("/usr/libexec/at-spi2/at-spi-bus-launcher", "/usr/lib/at-spi2-core/at-spi-bus-launcher")
        return
    
    pisitools.dodoc("NEWS", "README*")
