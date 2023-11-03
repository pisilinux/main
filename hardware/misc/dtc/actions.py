#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","1.7.0")

def setup():
    mesontools.configure("-Dstatic-build=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("GPL", "README*")
