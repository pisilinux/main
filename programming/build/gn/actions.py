#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.cd("build")
    shelltools.system("python ./gen.py --no-sysroot")
    
    shelltools.cd("..")
    shelltools.system("ninja -C out gn")

def install():
    pisitools.dobin("out/gn")

    pisitools.dodoc("AUTHORS", "LICENSE", "README*")
