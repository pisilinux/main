#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    options = "--disable-static \
               --disable-rpath \
               --disable-silent-rules \
               --disable-guile \
               --enable-heartbeat-support \
               --without-tpm \
               --disable-valgrind-tests"

    if get.buildTYPE() == "emul32":
        options += " --disable-hardware-acceleration \
                     --libdir=/usr/lib32 \
                     --bindir=/usr/emul32/bin \
                     --with-included-unistring \
                     --enable-local-libopts \
                   "

    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #some tests fail in emul32
    #if not get.buildTYPE() == "emul32":
        #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/emul32")
        return
    pisitools.dodoc("AUTHORS*", "README*")
        
