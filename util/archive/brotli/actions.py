#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="brotli-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)
    
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                          -DCMAKE_BUILD_TYPE=Release")

def build():
    cmaketools.make()
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -lbz2 -ldl")
    pythonmodules.compile(pyVer="3")
    
def check():
    cmaketools.make("test")
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.run("setup.py test", pyVer="3")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("LICENSE*")
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer="3")
