#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

WorkDir = "MarkupSafe-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="3")

def check():
    pythonmodules.compile("test", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

