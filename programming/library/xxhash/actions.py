#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools, shelltools

# WorkDir="xxHash-%s" % get.srcVERSION()

def setup():
    shelltools.system("export CFLAGS='$CFLAGS -DXXH_FORCE_MEMORY_ACCESS=1 -flto=auto -O2'")
    # shelltools.cd("%s" % get.workDIR())
    # shelltools.move("xxHash-*", "xxhash-%s" % get.srcVERSION())

    # shelltools.cd("boost-%s" % get.srcVERSION())

def build():
    autotools.make("PREFIX=/usr DISPATCH=1")


def install():
    # shelltools.system("make PREFIX=/usr DISPATCH=1 DESTDIR=%s install" % get.installDIR())
    autotools.install("PREFIX=/usr DISPATCH=1 DESTDIR=%s" % get.installDIR()), 0755
    pisitools.remove('/usr/lib/libxxhash.a')
    pisitools.dodoc("LICENSE", "doc/*")
