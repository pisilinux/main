#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6

def setup():
    kde6.configure("-DENABLE_CONSOLE=OFF \
                    -DENABLE_CLI=OFF \
                    -DENABLE_DOCS=OFF")

def build():
    kde6.make()

def install():
    kde6.install()

    #  Conflicts with kf5
    pisitools.removeDir("/usr/share/locale")

    pisitools.dodoc("COPYING*", "README*")
