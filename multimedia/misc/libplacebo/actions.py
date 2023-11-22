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
    mesontools.configure("-Dshaderc=disabled \
                                        -Ddemos=false \
                                        -Dxxhash=enabled \
                                        -Dlcms=enabled \
                                        -Dvulkan=enabled \
                                        -Dglslang=enabled \
                                        -Dd3d11=disabled \
                                        -Dlibdovi=disabled \
                                        -Dopengl=disabled")

def build():
    mesontools.build()

def install():
    mesontools.install()
    
    #shelltools.cd("..")
    pisitools.dodoc("RELEASING*", "LICENSE", "README*")
