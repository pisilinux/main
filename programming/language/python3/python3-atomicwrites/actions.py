#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pythonmodules.compile(pyVer="3")
    
def check():
    shelltools.system("PYTHONPATH=build:%s/python-atomicwrites-1.3.0/build/lib py.test" % get.workDIR())

def install():
    pythonmodules.install(pyVer="3")