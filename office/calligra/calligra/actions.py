#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5
from pisi.actionsapi import get

def setup():
    kde5.configure("-DPYTHON_EXECUTABLE=python3 \
                    -DBUILD_TESTING=OFF \
                    -DCMAKE_BUILD_TYPE=debugfull \
                    -DCMAKE_INSTALL_LIBDIR=lib \
                    -Wno-dev  \
                    -DBUILD_UNMAINTAINED=ON")

def build():
    kde5.make()

def install():
    kde5.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ANNOTATIONS-ODF", "AUTHORS", "COPYING*", "OBSOLETE.TXT", "README*", "TODO-ANNOTATIONS", "doc/status.txt")
