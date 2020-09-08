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
    shelltools.system('sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure')
    autotools.autoreconf("-vif")
    pisitools.cflags.add("-Wno-stringop-truncation \
                          -Wno-maybe-uninitialized")
    pisitools.cxxflags.add("-Wno-maybe-uninitialized")
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure \
                        --disable-nls \
                        --prefix=/build \
                        --enable-multilib \
                        --enable-interwork \
                        --enable-targets=all \
                        --enable-languages=all \
                        --with-guile=guile-2.0 \
                        --with-system-readline \
                        --with-python=/usr/bin/python \
                        --with-system-gdbinit=/etc/gdb/gdbinit")
#--disable-rpath
def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # to avoid conflict rename binaries
    pisitools.dodir("/usr/bin")
    pisitools.domove("/build/bin/gdb", "/usr/bin/", "gdb-multiarch")
    pisitools.removeDir("build")

    # 2020-04-09 To Do
    # Compile with Python3