 
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
  
    if get.buildTYPE() == "emul32":
      shelltools.system("./configure.py \
                       --prefix=/usr \
                       --pkgconfigdir=/usr/lib32/pkgconfig \
                       --libexecdir=/usr/lib32/clc \
                       --with-llvm-config=/usr/bin/llvm-config-32 \
                       --enable-runtime-subnormal \
                      ")    
    else:
      shelltools.system("./configure.py \
                       --prefix=/usr \
                       --pkgconfigdir=/usr/lib/pkgconfig \
                       --enable-runtime-subnormal \
                      ")
      

def build():
    
    
    autotools.make()

def install():
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("LICENSE.TXT","CREDITS.TXT", "README.TXT")