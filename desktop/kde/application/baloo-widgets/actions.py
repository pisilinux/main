#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

#WorkDir = "src"
def setup():
    #shelltools.makedirs("build")
    #shelltools.cd("build")
    kde5.configure()

def build():
    #shelltools.cd("..")
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("COPYING", "COPYING.LIB", "COPYING.README")
