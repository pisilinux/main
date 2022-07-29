#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system("../configure.py --prefix=/usr \
        --with-bzip \
        --with-lzma \
        --with-zlib \
        --with-boost \
        --with-sqlite3 \
        --with-os-feature=getrandom")
    
def build():
    shelltools.cd("build")
    autotools.make()

def check():
    shelltools.cd("build")
    autotools.make("check")
    #pass

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("COPYING*", "README")
