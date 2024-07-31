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
from pisi.actionsapi import cmaketools

WorkDir="%s" % get.srcDIR()

def setup():
    # create a folder for python3 build
    # shelltools.copy("python/",  "python3/")

    # suppress compiler warnings
    pisitools.cxxflags.add("-Wno-stringop-overflow -Wno-unused-function -Wno-deprecated-declarations")
    shelltools.export("PTHREAD_LIBS", "-lpthread")
    # shelltools.system("./autogen.sh")
    # autotools.autoreconf("-vif")
    cmaketools.configure("-D CMAKE_BUILD_TYPE=None \
                          -D CMAKE_INSTALL_PREFIX=/usr \
                          -D protobuf_BUILD_SHARED_LIBS=ON \
                          -D protobuf_USE_EXTERNAL_GTEST=ON \
                          -D protobuf_ABSL_PROVIDER=package")

    # fix unused direct dependency analysis
    # pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    cmaketools.make()
    # shelltools.cd("python")
    # pythonmodules.compile()
    # shelltools.cd("..")
    shelltools.cd("python")
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
    cmaketools.install()
    # shelltools.cd("python")
    # pythonmodules.install()
    # shelltools.cd("..")
    shelltools.cd("python")
    pythonmodules.install(pyVer="3")
    shelltools.cd("..")

    pisitools.insinto("/usr/share/vim/vimfiles/syntax/", "editors/proto.vim")
    pisitools.insinto("/usr/share/emacs/site-lisp/", "editors/protobuf-mode.el")

    pisitools.dodoc("LICENSE", "CONTRIBUTORS.txt", "LICENSE", "README.md")
