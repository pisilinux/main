#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="%s" % get.srcDIR()

def setup():
    # create a folder for python3 build
    shelltools.copy("python/",  "python3/")

    # suppress compiler warnings
    pisitools.cxxflags.add("-Wno-stringop-overflow -Wno-unused-function -Wno-deprecated-declarations")
    shelltools.export("PTHREAD_LIBS", "-lpthread")
    shelltools.system("./autogen.sh")
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    shelltools.cd("python")
    pythonmodules.compile()
    shelltools.cd("..")
    shelltools.cd("python3")
    pythonmodules.compile(pyVer="3")
    shelltools.cd("..")

# tests successfully completed but takes to much time!
#def check():
#    autotools.make("check")
#    shelltools.cd("python")
#    pythonmodules.compile("test")
#    shelltools.cd("..")
#    shelltools.cd("python3")
#    pythonmodules.compile("test", pyVer="3")
#    shelltools.cd("..")

def install():
    autotools.install()
    shelltools.cd("python")
    pythonmodules.install()
    shelltools.cd("..")
    shelltools.cd("python3")
    pythonmodules.install(pyVer="3")
    shelltools.cd("..")

    pisitools.insinto("/usr/share/vim/vimfiles/syntax/", "editors/proto.vim")
    pisitools.insinto("/usr/share/emacs/site-lisp/", "editors/protobuf-mode.el")

    pisitools.dodoc("CHANGES.txt", "CONTRIBUTORS.txt", "LICENSE", "README.md")
