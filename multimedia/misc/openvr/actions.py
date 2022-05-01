#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED=1 \
    -DUSE_SYSTEM_JSONCPP=True")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.domove("/usr/share/pkgconfig/openvr.pc","/usr/lib/pkgconfig")
    #pisitools.removeDir("/usr/share/pkgconfig")

    pisitools.dodoc("LICENSE", "README.md")
