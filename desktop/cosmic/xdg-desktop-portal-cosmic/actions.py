#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools



WorkDir="xdg-desktop-portal-cosmic-epoch-%s" % get.srcVERSION()

def setup():
    shelltools.system("cargo fetch --locked")
    

def build():
    shelltools.export("RUSTFLAGS", " -C link-arg=-fuse-ld=mold")
    # shelltools.system("jCARGO_NET_OFFLINE=true just build")
    shelltools.system('just build-release --frozen')


def install():

    shelltools.system("just rootdir=\"%s\" prefix='/usr' libexecdir='/usr/lib' install" % get.installDIR())
    
    pisitools.dodoc("LICENSE")
