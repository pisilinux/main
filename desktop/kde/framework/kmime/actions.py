#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kde6

def setup():
    shelltools.system("sed -e 's|KF_DEP_VERSION VERSION_LESS 6.27|TRUE|' -i CMakeLists.txt")
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("LICENSES/*", "README*")
