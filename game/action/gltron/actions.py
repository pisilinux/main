#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	#shelltools.system("sed -i 's/#include <ctype.h>/&\n#include <stdint.h>/' lua/src/lib/liolib.c")
	
	autotools.configure("--disable-warn \
                         --disable-debug \
                         --disable-profile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "COPYING")
