# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #pisitools.dosed("configure.ac", "pthread-stubs", deleteLine=True)
    autotools.autoreconf("-fi")
    options = " --enable-udev \
                --disable-cairo-tests"
     
    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32"
    
    autotools.configure(options)
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "_emul32":
        return
        
    #pisitools.dodoc("README")
