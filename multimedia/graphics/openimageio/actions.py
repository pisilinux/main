#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
     shelltools.makedirs("build")
     
     shelltools.cd("build")
     cmaketools.configure("-DUSE_QT=0  \
                           -DUSE_PYTHON=ON \
                           -DPYTHON_VERSION=2.7 \
                           -DCMAKE_INSTALL_PREFIX=/usr \
                           -DCMAKE_INSTALL_LIBDIR=lib \
                           -DPYLIB_INSTALL_DIR=lib/python2.7/site-packages \
                           -DUSE_OCIO= OFF \
                           -DUSE_OPENSSL:BOOL=TRUE \
                           -DSTOP_ON_WARNING:BOOL=FALSE \
                           -DOIIO_BUILD_TESTS=OFF", sourceDir="..")
     
def build():
    shelltools.cd("build")  
  
    cmaketools.make()

def install():
    shelltools.cd("build")
    
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    
    #pisitools.dodoc("CREDITS", "LICENSE", "README.*")
