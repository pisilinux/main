#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure(
        "-G Ninja"
    )

def build():
    shelltools.system("ninja")


def install():
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    pisitools.dodoc("LICENSE")