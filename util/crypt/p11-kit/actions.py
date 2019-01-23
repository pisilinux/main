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
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += "--prefix=/_emul32 \
                    --libdir=/usr/lib32 \
                    --libexecdir=/_emul32/libexec \
                    --with-module-path=/usr/lib32/pkcs11"
                 
                 
    autotools.configure(options)
 
      
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("_emul32")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
