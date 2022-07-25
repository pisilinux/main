#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file https://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get, mesontools, pisitools

def setup():
    mesontools.configure("--libexecdir=/usr/lib/%s \
                          -Dmathjax-directory=/usr/share/mathjax2 \
                          -Depub=true \
                          -Dcomics=true \
                          -Ddjvu=false \
                          -Ddvi=false \
                          -Dt1lib=true \
                          -Dpixbuf=true \
                          -Dhelp_files=true \
                          -Dintrospection=true" % get.srcNAME())

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
