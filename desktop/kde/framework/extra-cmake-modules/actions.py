#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed('kde-modules/KDEInstallDirs.cmake', '"lib64"', '"lib"')
    kde6.configure("-DBUILD_HTML_DOCS=OFF \
                    -DBUILD_MAN_DOCS=OFF")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("README.rst", "COPYING-CMAKE-SCRIPTS")
