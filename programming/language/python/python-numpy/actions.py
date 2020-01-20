#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "numpy-%s" % get.srcVERSION()

NUMPY_FCONFIG = "config_fc --fcompiler=gnu95"
shelltools.export("ATLAS", "None")
shelltools.export("PTATLAS", "None")
shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-unused-but-set-variable -Wno-builtin-declaration-mismatch \
                         -Wno-unused-value -Wno-unused-variable -Wno-unknown-pragmas \
                         -Wno-strict-prototypes -Wno-implicit-int -Wno-return-type \
                         -Wno-unused-function")
    pythonmodules.compile(NUMPY_FCONFIG)

def install():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-builtin-declaration-mismatch")
    pythonmodules.install(NUMPY_FCONFIG)
    
    pisitools.rename("/usr/bin/f2py", "f2py-py2")

    pisitools.dodoc("LICENSE*")
    
    for dirs in ["doc"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)