#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools, shelltools

def build():
    # shelltools.system('sed -i "s/fflit_core>=3.11,<4/flit_core>=3.11,<5/" pyproject.toml')
    pisitools.dosed("pyproject.toml", "flit_core>=3.11,<4", "flit_core>=3.11,<5")
    python3modules.compile(pyVer="3")

def install():
    python3modules.install(pyVer="3")
    pisitools.dodoc("LICENSE*")
