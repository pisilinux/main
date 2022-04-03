#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DENABLE_MAINTAINER_TOOLS=TRUE \
        -DENABLE_FONTFORGE_EXTRAS=TRUE \
        -DUNIX=TRUE", sourceDir="..")

def build():
    cmaketools.make("-C build")
    cmaketools.make("-C build doc")

def install():
    pisitools.dodoc("AUTHORS", "LICENSE", "README.md")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

