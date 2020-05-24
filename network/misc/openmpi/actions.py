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
    # Disable test causing sandbox violations
    #pisitools.dosed("test/util/Makefile.in", "^(check_PROGRAMS.*?)\sopal_path_nfs\$\(EXEEXT\)", "\\1")
    
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-unused-result -Wno-cpp -Wno-deprecated-declarations -Wno-stringop-overflow -Wno-discarded-qualifiers -Wno-alloc-size-larger-than")
    shelltools.export("LDFLAGS","%s -Wl,-z,noexecstack" % get.LDFLAGS())
    shelltools.export("FC", "/usr/bin/gfortran")
    autotools.configure("--with-valgrind \
                         --without-slurm \
                         --enable-mpi-cxx \
                         --with-hwloc=/usr \
                         --enable-memchecker \
                         --with-libltdl=/usr \
                         --enable-builtin-atomics \
                         --enable-mpi-fortran=all \
                         --sysconfdir=/etc/openmpi \
                         --libdir=/usr/lib/openmpi \
                         --enable-pretty-print-stacktrace")
    
    # dont touch rpath, it brokes tests
    #pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    #pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    # fix unused direct dependency analysis
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE","README*")
