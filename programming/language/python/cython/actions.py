#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    # fix unused dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    # compress compiler warnings
    shelltools.export("CFLAGS", "-fno-strict-aliasing -mtune=generic -march=x86-64 -O2 -pipe -fstack-protector -D_FORTIFY_SOURCE=2 -g -fPIC -fwrapv -DNDEBUG -g -fwrapv -O3 -Wno-strict-aliasing")
    pythonmodules.compile()

# it takes hours to run test, run with caution!
#def check():
#    pythonmodules.run("runtests.py -vv --no-pyregr")

def install():
    pythonmodules.install()
   
    for dirs in ["Doc", "Demos", "tests"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
       
    pisitools.dodoc("COPYING*", "README*", "USAGE*", "LICENSE*")
    pisitools.rename("usr/bin/cygdb", "cygdb-py2")
    pisitools.rename("usr/bin/cython", "cython-py2")
    pisitools.rename("usr/bin/cythonize", "cythonize-py2")