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
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-cpp")
    pisitools.cxxflags.add("-Wno-deprecated-copy -Wno-unused-parameter -Wno-deprecated-declarations")
    autotools.configure("--enable-shared --disable-static \
                         --with-quantum-depth=16 \
                         --with-sundials_ida='-lsundials_ida -lsundials_sunlinsolklu'")
    
    # don't fix rpath
    #pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    #pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "README*")
    
    #some packages search libraries direst under /usr/lib
    pisitools.dosym("/usr/lib/octave/5.2.0/liboctave.so.7.0.1", "/usr/lib/liboctave.so")
    pisitools.dosym("/usr/lib/octave/5.2.0/liboctinterp.so.7.0.1", "/usr/lib/liboctinterp.so")
    pisitools.dosym("/usr/lib/octave/5.2.0/liboctinterp.so.7.0.1", "/usr/lib/liboctinterp.so.7")