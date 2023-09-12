#!/usr/bin/env python
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
    mesontools.configure("-Dsystemdsystemunitdir=/tmp \
                                        -Dgtk_doc=true \
                                        --libexecdir=lib")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.removeDir("/tmp")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
