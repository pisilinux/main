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
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure \
                       --enable-tui \
                       --prefix=/usr \
                       --disable-nls \
                       --with-python \
                       --disable-rpath \
                       --with-guile=guile-2.0 \
                       --with-system-readline \
                       --enable-source-highlight \
                       --with-python=/usr/bin/python \
                       --with-gdb-datadir=/usr/share/gdb \
                       --with-system-gdbinit=/etc/gdb/gdbinit \
                       --with-separate-debug-dir=/usr/lib/debug")


def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # to prevent conflict with binutils delete these files:
    for libdel in ["libbfd.a", "libopcodes.a", "libctf.a", "libctf-nobfd.a"]:
        pisitools.remove("/usr/lib/%s" % libdel)

    for hea in ["ansidecl", "bfd", "bfdlink", "diagnostics", "dis-asm", "plugin-api", "symcat", "ctf", "ctf-api"]:
        pisitools.remove("/usr/include/%s.h" % hea)

    pisitools.remove("/usr/share/info/bfd.info")

    shelltools.cd("..")
    pisitools.dodoc("README*", "COPYING*", "ChangeLog*")
