#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    # pisitools.dosed("meson.build", "rest-0.7", "rest-1.0")
    # pisitools.dosed("src/gr-shopping-list-exporter.c", "rest/rest-oauth2-proxy.h", "rest-1.0/rest/rest-oauth2-proxy.h")
    # pisitools.dosed("src/gr-shopping-list-exporter.c", "rest/oauth2-proxy.h", "rest-1.0/rest/rest-oauth2-proxy.h")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "README.md")
