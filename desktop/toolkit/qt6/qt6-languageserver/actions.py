#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import qt6

def setup():
    # qt6.configure()
    cmaketools.configure("-B build -G Ninja \
                          -DCMAKE_MESSAGE_LOG_LEVEL=STATUS")

def build():
    qt6.make()

def install():
    qt6.install()

    pisitools.dodoc("LICENSES/*")
