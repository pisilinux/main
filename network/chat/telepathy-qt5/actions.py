#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "telepathy-qt-%s" % get.srcVERSION()

def setup():
    cmaketools.configure("-DDESIRED_QT_VERSION=5 \
                          -DPYTHON_EXECUTABLE=/usr/bin/python2.7 \
                          -DENABLE_EXAMPLES=OFF \
                          -DENABLE_TESTS=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
