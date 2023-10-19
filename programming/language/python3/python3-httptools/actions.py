#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="httptools-%s" % get.srcVERSION()

def setup():
    # install process needs some header files from
    # http-parser github repo. so we add that repo
    # and copy the header files to the corresponding path
    for files in ["../http-parser-2.9.4/*"]:
        shelltools.copy("%s" % files,"vendor/http-parser")

def build():
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
