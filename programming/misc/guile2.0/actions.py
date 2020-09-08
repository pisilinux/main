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
    autotools.autoreconf("-vif")
    autotools.configure("--enable-nls \
                         --enable-posix \
                         --with-modules \
                         --with-threads \
                         --enable-regex \
                         --disable-rpath \
                         --disable-static \
                         --enable-networking \
                         --program-suffix=2.0 \
                         --disable-error-on-warning")

    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # Put flags in front of the libs. Needed for --as-needed.
    #replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    #pisitools.dosed("libtool", *replace)
    #pisitools.dosed("*/libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.install()

    #major = ".".join(get.srcVERSION().split(".")[:2])
    #pisitools.dodir("/etc/env.d")
    #shelltools.echo("%s/etc/env.d/50guile" % get.installDIR(), 'GUILE_LOAD_PATH="/usr/share/guile/%s"' % major)
    
    # revove scm file
    pisitools.remove("/usr/lib/libguile-2.0.so.*.scm")
    #pisitools.domove("/usr/lib/libguile-2.0.so.*.scm", "/usr/share/gdb/auto-load")
    
    # remover info files to avoid conflicts
    pisitools.removeDir("/usr/share/info/")
    
    pisitools.rename("/usr/share/aclocal/guile.m4", "guile2.0.m4")
    pisitools.dodoc("COPYING*", "LICENSE", "HACKING", "README")