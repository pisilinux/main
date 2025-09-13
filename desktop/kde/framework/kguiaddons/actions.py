#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system('export SANDBOX_WRITE="/usr/lib/python3.11/site-packages"')
    kde6.configure("-DBUILD_GEO_SCHEME_HANDLER=OFF")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("README.md")
