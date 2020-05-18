#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules


def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    #autotools.autoreconf("-vfi")
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-missing-prototypes -Wno-format-truncation -Wno-implicit-fallthrough -Wno-cast-function-type -Wstringop-truncation")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    autotools.configure("--disable-silent-rules \
                         --disable-static \
                         --enable-perl \
                         --enable-ruby \
                         --enable-lua \
                         --enable-tcl \
                         --enable-python \
                         --with-rrd-default-font=/usr/share/fonts/dejavu/DejaVuSansMono.ttf \
                         --with-perl-options='installdirs=vendor destdir=%(DESTDIR)s' \
                         --with-ruby-options='sitedir=%(DESTDIR)s/usr/lib/ruby' \
                         " % {"DESTDIR": get.installDIR()})
 
    pisitools.dosed("Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    pisitools.dosed("doc/Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    pisitools.dosed("bindings/Makefile", "^RRDDOCDIR.*$", "RRDDOCDIR=${datadir}/doc/${PACKAGE}")
    pisitools.dosed("examples/Makefile", "examplesdir = .*$", "examplesdir = $(datadir)/doc/${PACKAGE}/examples")
    
    # TODO: fix rpath and unused direct dependency analysis
    
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s includedir=/usr/include" % get.installDIR())

    # remove unnecessary files
    perlmodules.removePacklist()
    perlmodules.removePodfiles()