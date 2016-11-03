# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    options = "-DVGL_FAKEXCB=1 \
               -DVGL_INCDIR=/usr/include \
               -DTJPEG_INCLUDE_DIR=/usr/include \
               -DVGL_DOCDIR=/usr/share/doc/%s \
               " % get.srcNAME()
    
    if get.buildTYPE() == "emul32":
      
      options += "-DVGL_LIBDIR=/usr/lib32 \
                  -DCMAKE_INSTALL_PREFIX=/emul32 \
                  -DVGL_BINDIR=/emul32/bin \
                  -DTJPEG_LIBRARY=/usr/lib32/libturbojpeg.so \
                  -DVGL_FAKELIBDIR=/usr/lib32/fakelib \
                 "
    elif get.ARCH() == "x86_64":
      
      options += "-DVGL_LIBDIR=/usr/lib \
                  -DCMAKE_INSTALL_PREFIX=/usr/share \
                  -DVGL_FAKELIBDIR=/usr/lib/fakelib \
                  -DCMAKE_INSTALL_PREFIX=/usr/share \
                  -DTJPEG_LIBRARY=/usr/lib/libturbojpeg.so \
                  -DVGL_BINDIR=/usr/bin"
      
      
    
    cmaketools.configure(options, sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
   

    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/bin/","%s/emul32/bin/glxspheres" % get.installDIR(),"glxspheres32")
        pisitools.removeDir("/emul32")    
        
        
    elif get.ARCH() == "x86_64":
        pisitools.domove("/usr/bin/glxinfo", "/usr/bin/", "vglxinfo")
    
