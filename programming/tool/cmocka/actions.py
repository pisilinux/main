#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DUNIT_TESTING=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()
    shelltools.cd("../doc")
    shelltools.system("doxygen mainpage.dox")
    
def check():
    shelltools.cd("build")
    autotools.make("test")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("../doc/html/*")

    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README*")