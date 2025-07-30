# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "--enable-ipv6 \
               --disable-static \
               --without-fop"

    if get.buildTYPE() == "emul32":
        options += " --disable-static"

    autotools.autoreconf("-vif")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*")
