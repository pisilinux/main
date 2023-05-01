#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure()
    
def build():
    cmaketools.make()

def install():
    cmaketools.install()

    # srt-devel
    pisitools.removeDir("/usr/lib/cmake/GTest")
    pisitools.removeDir("/usr/include/gmock")
    pisitools.removeDir("/usr/include/gtest")

    pisitools.remove("/usr/lib/pkgconfig/gtest_main.pc")
    pisitools.remove("/usr/lib/libgmock.a")
    pisitools.remove("/usr/lib/libgtest.a")
    pisitools.remove("/usr/lib/pkgconfig/gtest.pc")
    pisitools.remove("/usr/lib/pkgconfig/gmock.pc")
    pisitools.remove("/usr/lib/pkgconfig/gmock_main.pc")
    pisitools.remove("/usr/lib/libgtest_main.a")
    pisitools.remove("/usr/lib/libgmock_main.a")

