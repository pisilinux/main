#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX='/usr' \
        -DCMAKE_BUILD_TYPE='None' \
        -DJUCE_BUILD_EXTRAS=ON \
        -DJUCE_TOOL_INSTALL_DIR=bin \
        -DJUCER_ENABLE_GPL_MODE=1")

def build():
    cmaketools.make()

#def check():
    #cmaketools.make("test")


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("LICENSE.md", "README.md")
