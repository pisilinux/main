#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="requests-%s" % get.srcVERSION()

def install():
    shelltools.makedirs("python3")
    shelltools.copytree("../requests-%s" % get.srcVERSION(), "%s/python3" % get.workDIR())
    pythonmodules.install()
    shelltools.cd("%s/python3" % get.workDIR())
    pythonmodules.install(pyVer = "3")
