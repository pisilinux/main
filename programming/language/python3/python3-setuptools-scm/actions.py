#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir="setuptools_scm-%s" % get.srcVERSION()
#shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","7.1.0")

def build():
    python3modules.compile(pyVer="3")
    
    #python3modules.run("setup.py build_sphinx", pyVer="3")
    
# def check():
    # python3modules.compile("test", pyVer="3")

def install():
    python3modules.install(pyVer="3")
