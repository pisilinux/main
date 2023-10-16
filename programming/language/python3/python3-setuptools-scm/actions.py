#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","7.1.0")

def build():
    pythonmodules.compile(pyVer="3")
    
    #pythonmodules.run("setup.py build_sphinx", pyVer="3")
    
def check():
    pythonmodules.compile("test", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
