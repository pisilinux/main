#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules, shelltools, pisitools

def setup():
    pass
    # dodoc method cannot move LICENSE named dir, so i delete the directory
    shelltools.unlinkDir("LICENSE")
    pisitools.dosed("setupext.py", "LICENSE", deleteLine = True)

def build():
    # suppress compiler warnings:
    pisitools.cflags.add("-Wno-unused-but-set-variable -Wno-misleading-indentation -Wno-stringop-truncation -Wno-unused-function")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -lbz2")
    pythonmodules.compile(pyVer = "3")

def install():
    pythonmodules.install(pyVer = "3")
