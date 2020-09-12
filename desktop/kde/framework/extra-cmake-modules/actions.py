#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed('kde-modules/KDEInstallDirs.cmake', '"lib64"', '"lib"')
    kde5.configure("-DBUILD_HTML_DOCS=OFF \
                    -DBUILD_MAN_DOCS=OFF")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("README.rst", "COPYING-CMAKE-SCRIPTS")
