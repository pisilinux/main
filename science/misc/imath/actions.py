#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DPYTHON=ON \
                          -DDOCS=ON \
                          -DINSTALL_DOCS=OFF")

def build():
    cmaketools.make("-j2")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/Imath/sphinx/.doctrees")
    pisitools.remove("/usr/share/doc/Imath/sphinx/.buildinfo")

    pisitools.dodoc("CHANGES*", "LICENSE*", "README*")
