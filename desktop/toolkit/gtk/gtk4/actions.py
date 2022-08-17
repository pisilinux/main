#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools


def setup():
    mesontools.configure("-Dx11-backend=true \
                          -Dwayland-backend=true \
                          -Dbroadway-backend=true \
                          -Dman-pages=true \
                          -Dbuild-tests=false \
                          -Dmedia-ffmpeg=enabled \
                          -Dmedia-gstreamer=enabled \
                          -Dintrospection=enabled \
                          -Dcolord=enabled \
                          -Dcloudproviders=enabled \
                          -Dvulkan=enabled \
                          -Dgtk_doc=true")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.insinto("/usr/share/pixmaps/", "docs/tools/gtk-logo.png", "gtk4-logo.png")

    pisitools.rename("/usr/share/doc", "gtk-doc")
    pisitools.dodoc("AUTHORS", "README*", "COPYING*", "NEWS")
