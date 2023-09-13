#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    # Disable tracker 2.0 plugin
    pisitools.dosed("meson_options.txt", "'tracker',", " ")
    mesontools.configure("-Dapi-docs=false \
                                        -Dtests=false \
                                        -Dsystemd-user-units-dir=/tmp \
                                        -Dexamples=false")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.removeDir("/tmp")

    pisitools.dodoc("AUTHORS", "README*", "NEWS")
