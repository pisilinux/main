#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","3.5.0")

def build():
    pythonmodules.compile()
    
    #pythonmodules.run("setup.py build_sphinx")
    
def check():
    pythonmodules.compile("test")

def install():
    pythonmodules.install()