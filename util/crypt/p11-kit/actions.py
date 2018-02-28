#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "--with-module-path=/usr/lib/pkcs11 \
              "
              
    if get.buildTYPE() == "emul32":
        options += "--sysconfdir=/usr/emul32/etc \
                    --bindir=/usr/emul32/bin \
                    --libdir=/usr/lib32 \
                    --datadir=/usr/emul32/share \
                    --with-module-path=/usr/lib32/pkcs11 \
                    --libexecdir=/usr/emul32/libexec"
        
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
                 
                 
    autotools.configure(options)
 
      
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/emul32")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
