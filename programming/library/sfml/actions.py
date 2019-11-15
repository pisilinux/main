#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DSFML_USE_SYSTEM_DEPS=ON \
		                  -DSFML_BUILD_EXAMPLES=1 \
		                  -DSFML_BUILD_DOC=1 \
		                  -DSFML_INSTALL_PKGCONFIG_FILES=1 \
		                  ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("changelog.md", "license.md", "readme.md")
