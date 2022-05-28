#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

NoStrip=["/usr/local"]

def setup():
    mesontools.configure("-D b_lto=true -D b_ndebug=true -D prebuilt_server='%s/scrcpy-server-v1.24'" % get.workDIR())

def build():
    mesontools.build()

def check():
    mesontools.build("test")


def install():
    mesontools.install()

    pisitools.dodoc("LICENSE", "README*")
