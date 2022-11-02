#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Ddocs=false \
                          -Dman=true \
                          -Dstemmer=disabled \
                          -Dsystemd_user_services=false \
                          -Dsystemd_user_services_dir=no \
                          -Dunicode_support=icu")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING*", "HACKING.md", "MAINTAINERS", "NEWS", "README*")
