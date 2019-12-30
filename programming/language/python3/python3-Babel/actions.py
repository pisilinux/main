#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("mkdir -p cldr")
    shelltools.system("cp core.zip cldr/cldr-core-35.1.zip")

def build():
    pythonmodules.run("setup.py import_cldr", pyVer="3")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.dohtml("docs/")