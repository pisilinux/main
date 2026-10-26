#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools


def build():
    # shelltools.system('sed -i "s/flit_core >=3.12,<4/flit_core >=3.12,<5/" pyproject.toml')
    python3modules.compile(pyVer="3")
    
#def check():
#    shelltools.system("nosetests3")

def install():
    python3modules.install(pyVer="3")
