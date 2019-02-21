#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    options = "--disable-static \
                    --with-pic"
                    
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
    
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("README")
