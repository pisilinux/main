#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-unused-result -Wno-stringop-overflow")
    shelltools.system("MAKEINFO=/usr/bin/makeinfo  WX_CONFIG=/usr/bin/wx-config ./configure --prefix=/usr \
                       --libexecdir=/usr/bin \
                       --with-gihdir=/usr/share/gnuplot \
                       --with-readline=gnu \
                       --with-bitmap-terminals \
                       --with-wx-single-threaded \
                       --with-caca \
                       --with-texdir=/usr/share/texmf/tex/latex/gnuplot")

def build():
    autotools.make("pkglibexecdir=/usr/bin")

def install():
    autotools.rawInstall("pkglibexecdir=/usr/bin DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("Copyright", "README*")
