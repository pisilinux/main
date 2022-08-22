#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed 's@/bin/sh@/bin/sh -l@' -i gnome-session/gnome-session.in")
    shelltools.system("""sed -i "/  systemd_dep/,+3d;/if enable_systemd/a \ " meson.build""")

    mesontools.configure("--buildtype=release \
                          -Dsystemd=false \
                          -Dsystemd_session=disable \
                          -Dsystemd_journal=false")

def build():
    mesontools.build()

def install():
    mesontools.install()

    #shelltools.system("rm -rv %s/tmp/{*.d,*.target,*.service}" % get.installDIR())
