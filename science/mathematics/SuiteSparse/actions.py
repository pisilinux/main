#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def build():
    shelltools.system("BLAS=-lblas LAPACK=-llapack TBB=-ltbb SPQR_CONFIG=-DHAVE_TBB MY_METIS_LIB=/usr/lib/libmetis.so make")

def install():
    shelltools.system("BLAS=-lblas LAPACK=-llapack TBB=-ltbb SPQR_CONFIG=-DHAVE_TBB MY_METIS_LIB=/usr/lib/libmetis.so \
                       make INSTALL_LIB=%s/usr/lib INSTALL_INCLUDE=%s/usr/include install" % (get.installDIR(), get.installDIR()))
    
    # fix rpath
    shelltools.system("chrpath -d %s/usr/lib/*" % get.installDIR())
    
    pisitools.dodoc("LICENSE*", "README*")
