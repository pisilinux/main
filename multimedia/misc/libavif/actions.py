#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DAVIF_BUILD_APPS=ON \
                          -DAVIF_CODEC_AOM=ON \
                          -DAVIF_CODEC_DAV1D=ON \
                          -DAVIF_CODEC_SVT=ON \
                          -DAVIF_CODEC_RAV1E=ON \
                          -DAVIF_BUILD_GDK_PIXBUF=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
