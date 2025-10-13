# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#WorkDir = "mozjs%s/js/src" % get.srcVERSION()
ObjDir = "obj"
shelltools.export("SHELL","/bin/sh")
WorkDir = "firefox-%s" %get.srcVERSION()


shelltools.system("export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=pip")
shelltools.export("MOZBUILD_STATE_PATH", "mozbuild")
shelltools.system("export MOZ_NOSPAM=1")

def setup():
   # shelltools.export("CC", "gcc")
   # shelltools.export("CXX", "g++")
   # shelltools.system("cp mozconfig .mozconfig")
   shelltools.system("cp mozconfig js/src/.mozconfig")


def build():
    # shelltools.cd("build-js")
    shelltools.system("./mach build")


def install():
    shelltools.system("DESTDIR=%s ./mach install " % get.installDIR())
    pisitools.remove("/usr/lib/*.ajs")

    pisitools.dosym("/usr/lib/libmozjs-140.so", "/usr/lib/libmozjs-140.so.0")

    pisitools.dodoc("README*")

    # add link for polkit
    #pisitools.dosym("libmozjs-..so", "/usr/lib/libmozjs-17.0.so")
