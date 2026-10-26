#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools

def check():
    # shelltools.system("nosetests3 --with-doctest -e documentation")
    python3modules.compile()

def install():
    python3modules.install()
