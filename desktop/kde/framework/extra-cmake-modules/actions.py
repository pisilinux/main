#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_HTML_DOCS=OFF \
                          -DBUILD_MAN_DOCS=OFF", sourceDir=".")

def build():
    cmaketools.make()    

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
        
    pisitools.dodoc("README.rst", "COPYING-CMAKE-SCRIPTS")
    