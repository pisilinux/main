#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    #shelltools.system("sed -r 's/^install:.*/install:/;/install.*STATICLIB/d' -i Makefile")
    autotools.configure("--with-openmp")

def build():
    autotools.make("shared imagequant.pc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*", "COPYING", "ANNOUNCE")