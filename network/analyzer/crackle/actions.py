#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.make()

def install():
    pisitools.dosbin("crackle", "usr/local/bin")
    pisitools.dodoc("AUTHORS", "COPYING", "README")
