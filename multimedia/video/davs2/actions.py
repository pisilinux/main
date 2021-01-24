#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("patch -p1 --binary < davs2-1.6-gcc8-fix.patch")
    shelltools.cd("build/linux")
    autotools.configure("--extra-ldflags='-Wl,-z,noexecstack' \
                         --chroma-format='all' \
                         --enable-shared ")

def build():
    shelltools.cd("build/linux")
    autotools.make()

def install():
    shelltools.cd("build/linux")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../..")
    pisitools.dodoc("COPYING", "README.md")

