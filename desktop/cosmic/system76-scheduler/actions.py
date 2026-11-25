#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


# def setup():
    # shelltools.system('cargo fetch --locked')

def build():
    shelltools.system('export CC=clang')
    shelltools.system('just build-release')


def install():
    shelltools.system("just rootdir='%s' install" % get.installDIR())

    pisitools.dodoc("LICENSE*")
