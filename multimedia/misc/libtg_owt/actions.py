#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("tg_owt-*", "tg-owt-%s" % get.srcVERSION())
    shelltools.cd("tg-owt-%s" % get.srcVERSION())
    
    shelltools.move("../libvpx/*", "src/third_party/libvpx/source/libvpx")
    shelltools.move("../libyuv/*", "src/third_party/libyuv")
    
    shelltools.system("mkdir build")
    shelltools.cd("build")
    cmaketools.configure("-DBUILD_SHARED_LIBS=TRUE \
                        -DTG_OWT_PACKAGED_BUILD=TRUE \
                        -DTG_OWT_USE_PROTOBUF=TRUE", sourceDir="..")

def build():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("tg-owt-%s/build" % get.srcVERSION())
    cmaketools.make()

def install():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("tg-owt-%s/build" % get.srcVERSION())
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("../LICENSE")
