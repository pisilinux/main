#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    autotools.make("PREFIX='/usr'")
    shelltools.system("sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE")
    shelltools.system("sed -i '1,22s/^.\{,3\}//' LICENSE")

def install():
    autotools.rawInstall("PREFIX='/usr' DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("LICENSE")


