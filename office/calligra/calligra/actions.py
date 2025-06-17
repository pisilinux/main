#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6
from pisi.actionsapi import get

def setup():
    kde6.configure("-DPYTHON_EXECUTABLE=python3 \
                    -DBUILD_TESTING=OFF \
                    -DCMAKE_BUILD_TYPE=debugfull \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -Wno-dev  \
                    -DQT_MAJOR_VERSION=6 \
                    -DBUILD_UNMAINTAINED=ON")

def build():
    kde6.make()

def install():
    kde6.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ANNOTATIONS-ODF", "AUTHORS", "COPYING*", "OBSOLETE.TXT", "README*", "TODO-ANNOTATIONS", "LICENSES/*", "doc/status.txt")
