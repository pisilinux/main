#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("-Dgtkdoc=true \
                         --libexecdir=/usr/lib")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.dodoc("LICENSE", "README*")
    # remove installed tests
    pisitools.removeDir("/usr/lib/installed-tests/")
    pisitools.removeDir("/usr/share/installed-tests/")