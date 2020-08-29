#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # rename binary "wheel"
    pisitools.rename("/usr/bin/wheel", "wheel-py2")