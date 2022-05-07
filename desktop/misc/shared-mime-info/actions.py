#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


def setup():
    # https://bugs.freedesktop.org/show_bug.cgi?id=70366
    #shelltools.export("ac_cv_func_fdatasync", "no")

    shelltools.copy("../xdgmime-*/*", "xdgmime")

    autotools.make("-C xdgmime")

    mesontools.configure("-Dupdate-mimedb=false -D xdgmime-path=%s/xdgmime" % get.srcDIR())
     
def build():
    mesontools.build()

def check():
    mesontools.build("test")

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "NEWS", "README*")
