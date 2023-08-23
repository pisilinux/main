#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("--libexecdir=lib \
                                        -Dstemming=false \
                                        -Dqt=true \
                                        -Dvapi=true")
    
   
def build():
    mesontools.build()
    
def install():
    mesontools.install()


    pisitools.insinto("/usr/share/pixmaps/", "docs/images/src/png/appstream-logo.png")
    
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")
