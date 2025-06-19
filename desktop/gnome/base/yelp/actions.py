#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    mesontools.configure()


def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "TODO", "README*", "NEWS", "ChangeLog", "AUTHORS")
