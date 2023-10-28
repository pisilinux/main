#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    python3modules.compile(pyVer="3")
    
# def check():
    # shelltools.system("PYTHONPATH=build:%s/python-atomicwrites-1.4.1/build/lib py.test" % get.workDIR())

def install():
    python3modules.install(pyVer="3")
