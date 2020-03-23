#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def build():
    pythonmodules.compile(pyVer="3")
    
def check():
    pythonmodules.compile("test", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
