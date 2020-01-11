#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "yaml-%s" % get.srcVERSION()

def setup():
    pisitools.cflags.add("-Wno-unused-value -Wno-enum-compare")
    autotools.autoreconf("-fvi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("LICENSE", "README")
