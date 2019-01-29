#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    
    options = " --disable-static \
              "
    
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                   "
        
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if not get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("NEWS", "README.md", "LICENSE")
