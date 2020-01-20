#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

def build():
    # suppress compiler warnings:
    pisitools.cflags.add("-Wno-format -Wno-comment -Wno-unused -Wno-incompatible-pointer-types \
                         -Wno-logical-not-parentheses -Wno-bool-compare -Wno-maybe-uninitialized \
                         -Wno-discarded-qualifiers -Wno-pointer-sign -Wno-pointer-to-int-cast \
                         -Wno-unknown-pragmas")
    # fix unused dependency analysis:
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.insinto(docdir, "docs", "examples")