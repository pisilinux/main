#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt
#
# TODO: fix grilo support

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    # pisitools.dosed("meson.build", "gcr-base-3", "gcr-4")
    mesontools.configure("-Dsnap=false \
                          -Dx11=true \
                          -Ddistributor_logo=/usr/share/pixmaps/gnome-control-center-pisilinux-logo.svg \
                          -Ddark_mode_distributor_logo=/usr/share/pixmaps/gnome-control-center-pisilinux-logo-dark.svg")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("NEWS", "README*", "COPYING")
