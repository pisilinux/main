#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    # Disable tracker 2.0 plugin
    pisitools.dosed("meson_options.txt", "'tracker',", " ")
    #pisitools.dosed("meson.build", "gupnp-1.2", "gupnp-1.6")
    #pisitools.dosed("meson.build", "gssdp-1.2", "gssdp-1.6")
    #pisitools.dosed("meson.build", "0.14.1", "0.14.0")
    mesontools.configure("-Dapi-docs=false \
                          -Dtests=false \
                          -Dexamples=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
