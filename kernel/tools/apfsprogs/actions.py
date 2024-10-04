#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

MAKEFLAGS = 'GIT_COMMIT=f31d7c2 \
             DESTDIR=%(prefix)s/%(defaultprefix)s' % {
                                                         'prefix': get.installDIR(),
                                                         'defaultprefix': get.defaultprefixDIR(),
                                                     }

def build():
    autotools.make("-C lib")
    autotools.make("-C apfs-label %s" % MAKEFLAGS)
    autotools.make("-C apfs-snap %s" % MAKEFLAGS)
    autotools.make("-C apfsck %s" % MAKEFLAGS)
    autotools.make("-C mkapfs %s" % MAKEFLAGS)

def install():
    autotools.install("-C apfs-label %s" % MAKEFLAGS)
    autotools.install("-C apfs-snap %s" % MAKEFLAGS)
    autotools.install("-C apfsck %s" % MAKEFLAGS)
    autotools.install("-C mkapfs %s" % MAKEFLAGS)

    pisitools.dodoc("LICENSE", "README*")
