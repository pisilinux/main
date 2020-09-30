#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = ''.join([
              '-Wno-unused-result ',
              '-Wno-format-overflow ',
              '-Wno-deprecated-declarations'
              ])

    # gamin's optional-ness is overstated
    shelltools.system("sed -i 's|^.*<fam.h>|//&|' gschem/src/gschem_change_notification.c")
    shelltools.system("sed -i 's| enum FAMCodes | int |' gschem/src/gschem_change_notification.c")
    #autotools.autoreconf("-vfi")
    # xorn uses python2 instead of python, shebang problems
    shelltools.export("PYTHON_CFLAGS", "-I/usr/include/python2.7/")
    shelltools.export("PYTHON_LIBS", "-lpython2.7")
    # to fix cannot find libguile.h error
    shelltools.export("GUILE_CFLAGS", "-I/usr/include/guile/2.2/")
    shelltools.export("GUILE_LIBS", "-lguile-2.2")
    
    pisitools.cflags.add("%s" % options)
    autotools.configure("--prefix=/usr \
                         --disable-rpath \
                         --without-libfam \
                         --docdir=/usr/share/doc \
                         --localedir=/usr/share/locale \
                         --disable-update-xdg-database")
    
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    pisitools.dosed("xorn/libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README")
