#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import get
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
def setup():
    mesontools.configure("--prefix=/usr \
                          --buildtype=plain \
                          -Ddeprecated_warnings=false \
                          -Denable_debug=false")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")
