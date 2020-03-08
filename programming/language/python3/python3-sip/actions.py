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
    shelltools.copytree("../sip-%s" % (get.srcVERSION().replace("_", "~")), "../sip-%s-pyqt5" % get.srcVERSION())
    
    shelltools.system("find . -type f -exec sed -i 's/Python.h/python3.6m\/Python.h/g' {} \;")
    
    pythonmodules.run('configure.py CFLAGS="%s" CXXFLAGS="%s"' % (get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")
    
    shelltools.cd("../sip-%s-pyqt5" % get.srcVERSION())    
    pythonmodules.run('configure.py CFLAGS="%s" CXXFLAGS="%s" --sip-module PyQt5.sip --no-tools' % (get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")
                        

def build():
    autotools.make()
    
    shelltools.cd("../sip-%s-pyqt5" % get.srcVERSION())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("../sip-%s-pyqt5" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
