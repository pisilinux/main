#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os


def setup():

    shelltools.system("sed 's| -Werror||' -i CMakeLists.txt")
    cmaketools.configure("-DCDOGS_DATA_DIR=/usr/share/cdogs/")


def build():

    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())

    pisitools.dodoc("doc/AUTHORS", "doc/COPYING.GPL", "doc/original_readme.txt", "doc/README_DATA.md")
