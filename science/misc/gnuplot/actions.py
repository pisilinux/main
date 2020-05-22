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
    # fix default source location; use the GDFONTPATH variable to modify at runtime
    shelltools.system("sed -i 's|/usr/X11R6/lib/X11/fonts/truetype|/usr/share/fonts/TTF|' src/variable.c")
    shelltools.system("sed -i -e 's|/usr/X11R6/lib/X11/fonts/Type1|/usr/share/fonts/Type1|' \
                              -e 's|$(X11ROOT)/X11R6/lib/X11/fonts/Type1|$(X11ROOT)/usr/share/fonts/Type1|' \
                              src/variable.c")
    
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-unused-result -Wno-stringop-overflow")
    shelltools.system("MAKEINFO=/usr/bin/makeinfo  WX_CONFIG=/usr/bin/wx-config ./configure --prefix=/usr \
                       --libexecdir=/usr/bin \
                       --with-gihdir=/usr/share/gnuplot \
                       --with-readline=gnu \
                       --with-bitmap-terminals \
                       --with-wx-single-threaded \
                       --with-texdir=/usr/share/texmf/tex/latex/gnuplot")

def build():
    autotools.make("pkglibexecdir=/usr/bin")

def install():
    autotools.rawInstall("pkglibexecdir=/usr/bin DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("Copyright", "README*")