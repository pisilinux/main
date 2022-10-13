#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

#WorkDir = "sip-%s" % get.srcVERSION()

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("sip-%s" % get.srcVERSION())
    shelltools.copytree("../sip-%s" % (get.srcVERSION().replace("_", "~")), "../sip-%s-pyqt6" % get.srcVERSION())
    
    # shelltools.system("find . -type f -exec sed -i 's/Python.h/python3.9\/Python.h/g' {} \;")
    
    # pythonmodules.compile(pyVer="3")
    
    # shelltools.cd("../sip-%s-pyqt6" % get.srcVERSION())
    # pythonmodules.compile(pyVer="3")
                        

def build():
    pythonmodules.compile(pyVer="3")
    
    shelltools.cd("../sip-%s-pyqt6" % get.srcVERSION())
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("../sip-%s-pyqt6" % get.srcVERSION())
    pythonmodules.install(pyVer="3")
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())
