#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-3.0.txt


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ladspa_sdk_%s/src" % get.srcVERSION()

def setup():
    pisitools.dosed("Makefile", "-Werror", get.CFLAGS())

def build():
    autotools.make('CC="%s" \
                    CXX="%s" \
                    LD="%s" \
                    targets' % (get.CC(), get.CXX(), get.LD()))

def install():
    autotools.install('INSTALL_PLUGINS_DIR="%s/usr/lib/ladspa" \
					   INSTALL_INCLUDE_DIR="%s/usr/include" \
					   INSTALL_BINARY_DIR="%s/usr/bin" \
                       MKDIR_P="mkdir -p" \
                       DESTDIR="%s" \
                       ' % (get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR()))

    shelltools.cd("..")
    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/COPYING","doc/ladspa.h.txt")
