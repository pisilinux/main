#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt
# TODO: Add libchamplain (Contact Maps) support.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("CMakeLists.txt", "webkit2gtk-4.1", "webkit2gtk-5.0")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DSYSCONF_INSTALL_DIR=/etc \
                          -DENABLE_INSTALLED_TESTS=OFF \
                          -DENABLE_PST_IMPORT=OFF \
                          -DENABLE_YTNEF=OFF \
                          -DENABLE_CONTACT_MAPS=OFF \
                          -DENABLE_TEXT_HIGHLIGHT=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "HACKING", "MAINTAINERS", "NEWS", "README.md")
