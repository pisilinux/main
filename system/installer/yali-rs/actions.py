#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system('cargo fetch')

def build():
    shelltools.system('make')


def install():
    shelltools.system("make DESTDIR=%s install" % get.installDIR())

    pisitools.dodoc("LICENSE*", "README*")
