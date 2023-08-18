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
    shelltools.system("sed -i -e '/gtk4-update-icon-cache/d' tools/meson.build || die")
    shelltools.system("sed -i -e 's/^ld =.*/ld = disabler()/g' gtk/meson.build demos/gtk-demo/meson.build demos/widget-factory/meson.build || die")
    shelltools.system("sed -i -e 's/^objcopy =.*/objcopy = disabler()/g' gtk/meson.build demos/gtk-demo/meson.build demos/widget-factory/meson.build || die")

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
                          -Ddocumentation=true")
                            # -Dvulkan=enabled \

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.insinto("/usr/share/pixmaps/", "docs/reference/gtk/images/gtk-logo.png", "gtk4-logo.png")

    pisitools.rename("/usr/share/doc", "gtk-doc")
    pisitools.dodoc("AUTHORS", "README*", "COPYING*", "NEWS")
