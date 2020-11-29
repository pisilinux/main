#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    options = "--builtin-libraries=replace \
               --bundled-libraries=NONE \
               --disable-rpath \
              "
              
    if get.buildTYPE() == "_emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " --libdir=/usr/lib32 \
                     --bindir=/usr/bin32 \
                     --disable-python \
                   "
    else: shelltools.export("LDFLAGS", "-lpthread")
    autotools.configure(options)

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "_emul32":
        pisitools.removeDir("usr/bin32")
        return
    
    pisitools.dodoc("docs/README")
