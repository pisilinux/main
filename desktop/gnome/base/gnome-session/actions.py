#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dsystemd=false \
                          -Dsystemd_session=disable \
                          -Dsystemd_journal=false \
                          -Delogind=true")

def build():
    mesontools.build()

def install():
    mesontools.install()
