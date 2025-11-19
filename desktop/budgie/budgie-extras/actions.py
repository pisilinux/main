#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("find . -name meson.build -exec sed -i -e 's/budgie-1.0/budgie-2.0/' -e 's/libpeas-1.0/libpeas-2/' -e '/libpeas-gtk-1.0/d' {} +")
    mesontools.configure("-D b_pie=false")

def build():
    mesontools.build()
    
def install():
    mesontools.install()
    
    pisitools.dodoc("README*", "LICENSE")
