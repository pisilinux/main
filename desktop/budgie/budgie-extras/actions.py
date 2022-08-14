#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system("sed -i -e 's:T1_initLib:T1_InitLib:' meson.build || die")
    mesontools.configure("-D b_pie=false")

def build():
    mesontools.build()
    
def install():
    mesontools.install()
    
    pisitools.dodoc("README*", "LICENSE")
