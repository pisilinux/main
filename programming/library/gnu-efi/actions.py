#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pisitools.ldflags.remove("-Wl,-z,relro")
    pisitools.ldflags.remove("-Wl,-O1")
    pisitools.ldflags.remove("-Wl,--hash-style=gnu")
    pisitools.ldflags.remove("-Wl,--as-needed")
    pisitools.ldflags.remove("-Wl,--sort-common")
    shelltools.system("sed -e 's/-Werror//g' -i Make.defaults")

    options="PREFIX='/usr' lib gnuefi inc apps"
    autotools.make(options)


def install():
    autotools.rawInstall("INSTALLROOT=%s \
                          PREFIX='/usr'"  % get.installDIR())
