#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure(" -DCMAKE_INSTALL_PREFIX=/usr \
        -DRAPIDJSON_HAS_STDSTRING=ON \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        -DRAPIDJSON_BUILD_EXAMPLES=OFF \
        -DRAPIDJSON_BUILD_TESTS=OFF \
        -DRAPIDJSON_BUILD_THIRDPARTY_GTEST=OFF \
        -DCMAKE_BUILD_TYPE=None ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
