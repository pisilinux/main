#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools, mesontools

def setup():
    options = "-Dmodule_path=/usr/lib/pkcs11 \
               -Dtrust_paths=/etc/ssl/certs/ca-certificates.crt \
               -Dman=true -Dgtk_doc=true \
              "
              
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " --libdir=/usr/lib32 \
                    --libexecdir=/_emul32/libexec \
                    --bindir=/_emul32/bin \
                    -Dmodule_path=/usr/lib32/pkcs11"
                 
                 
    mesontools.configure(options)
 
      
def build():
    mesontools.build()

def install():
    mesontools.install()

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("_emul32")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
