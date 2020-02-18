#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()
    autotools.make("zstdmt")
    autotools.make("-C contrib/pzstd")
    
def check():
    autotools.make("check")
    autotools.make("-C contrib/pzstd test")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    pisitools.dobin("zstdmt")
    pisitools.dobin("contrib/pzstd/pzstd")

    pisitools.dodoc("CONTRIBUTING*", "CHANGELOG*", "COPYING", "LICENSE", "README*")
