#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, shelltools
from pisi.actionsapi import pisitools, cmaketools
from pisi.actionsapi import get


WorkDir = "SFML-2.5.1"

def setup():
    shelltools.system("mkdir build")
    shelltools.system("cd build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
      -DSFML_USE_SYSTEM_DEPS=ON \
      -DSFML_BUILD_EXAMPLES=1 \
      -DSFML_BUILD_DOC=1 \
      -DSFML_INSTALL_PKGCONFIG_FILES=1")

def build():
    cmaketools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/licenses/sfml/LICENSE", "license.md")
