#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    # shelltools.system("sh ./autogen.sh")
    # autotools.configure("--includedir=/usr/include \
                         # --with-extdict-{ru,zh,zhy}")

    cmaketools.configure("-B build -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE='None' \
        -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
        -DBUILD_SHARED_LIBS=ON \
        -DESPEAK_COMPAT=ON \
        -DESPEAK_BUILD_MANPAGES=ON")

def build():
    # autotools.make("src/espeak-ng src/speak-ng")
    # autotools.make("-j1")
    cmaketools.make("-C build")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # pisitools.rename("/usr/bin/speak", "speak-ng")
    # pisitools.rename("/usr/bin/espeak", "espeak-ng")
    pisitools.remove("/usr/bin/espeak")
    pisitools.removeDir("/usr/include/espeak")

    shelltools.cd("..")
    pisitools.dodoc("COPYING*", "ChangeLog*", "README*")
