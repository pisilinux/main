#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

def setup():
    shelltools.system("""sed -i -r 's:"(/system):"/org/gnome\1:g' schemas/*.in""")
    mesontools.configure()

def build():
    mesontools.build

def install():
    mesontools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "MAINTAINERS")


