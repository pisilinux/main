#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    # shelltools.export("CARGO_PROFILE_RELEASE_DEBUG", "2")
    # shelltools.export("CARGO_PROFILE_RELEASE_STRIP", "false")
    # shelltools.export("CARGO_PROFILE_RELEASE_LTO", "true")
    # shelltools.export("CARGO_PROFILE_RELEASE_CODEGEN_UNITS", "1")
    # shelltools.system("""cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')" """)

    mesontools.configure()
    

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "README.md")
