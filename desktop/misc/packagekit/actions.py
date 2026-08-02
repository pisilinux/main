#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dpackaging_backend=pisi \
                          -Ddaemon_tests=false \
                          -Dbash_completion=false \
                          -Dman_pages=false \
                          -Dsystemd=false \
                          -Delogind=false \
                          -Doffline_update=false \
                          -Dlegacy_tools=true \
                          -Dgstreamer_plugin=false \
                          -Dgtk_module=false \
                          -Dbash_command_not_found=false \
                          -Dcron=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS")
