#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("cmake -B build \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                        ")
     
def build():
    shelltools.cd("build")
    cmaketools.make()

#def check():
    #autotools.make("check")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
