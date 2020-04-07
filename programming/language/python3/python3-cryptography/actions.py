#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-stringop-truncation -Wno-deprecated-declarations -Wno-incompatible-pointer-types -Wno-discarded-qualifiers -Wno-sign-conversion -Wno-sign-compare")
    pythonmodules.compile(pyVer="3")
    # build documentation
    shelltools.cd("docs")
    autotools.make("html")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.dohtml("docs/_build/html/*")
    
    #for dirs in ["vectors"]:
    #    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)