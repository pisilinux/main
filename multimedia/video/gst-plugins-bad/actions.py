#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    mesontools.configure("-Dpackage-name='PisiLinux gstreamer-plugins-bad package' \
                          -Dpackage-origin='https://www.pisilinux.org' \
                          -D msdk=disabled")

def build():
    mesontools.build()
    
def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README*", "RELEASE", "REQUIREMENTS")
