#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    python3modules.compile()

def install():
    python3modules.install()
    pisitools.remove("/usr/lib/python3*/site-packages/pyudev/pyside.py")
