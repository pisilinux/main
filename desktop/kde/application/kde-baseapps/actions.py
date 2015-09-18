#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde5

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("README", "COPYING.LIB")