#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    #shelltools.system("""sed -i "s/ '--ignore-installed',//" pep517/envbuild.py""")
    python3modules.compile(pyVer="3")

def install():
    python3modules.install(pyVer="3")

    pisitools.dodoc("LICENSE", "README*")
