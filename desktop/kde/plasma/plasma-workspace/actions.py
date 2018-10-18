#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #shelltools.system("sed -i 's|5.11.0|5.10.0|g' CMakeLists.txt")
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()
    #pisitools.dosym("/usr/lib/drkonqi", "/usr/lib/libexec/drkonqi")

    pisitools.dodoc("COPYING", "HACKING")
