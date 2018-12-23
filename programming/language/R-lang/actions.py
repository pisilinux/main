#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("R_HOME_DIR", "/usr/lib/R")
    shelltools.export("BLAS_LIBS","/usr/lib")
    shelltools.export("LAPACK_LIBS","-L/usr/lib -llapack -lblas")

    autotools.aclocal("-I m4")
    autotools.autoconf()
    autotools.configure("--prefix=/usr \
                         --libdir=/usr/lib \
                         --sysconfdir=/etc/R \
                         --datarootdir=/usr/share \
                         --with-recommended-packages \
                         --enable-R-profiling \
                         --enable-R-shlib \
                         --enable-shared \
                         --enable-prebuilt-html \
                         --disable-openmp \
                         --with-blas=-lblas \
                         --with-lapack \
                         --without-tcltk \
                         --with-readline \
                         rsharedir=/usr/share/R/ \
                         rdocdir=/usr/share/doc/R \
                         rincludedir=/usr/include/R \
                         --with-x")

def build():
    shelltools.export("R_HOME","")
    autotools.make()

    # build math library
    shelltools.cd("src/nmath/standalone")
    autotools.make("shared")

#def check():
    #shelltools.export("R_HOME","")
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # install math library remove static libs
    autotools.rawInstall("-C src/nmath/standalone DESTDIR=%s" % get.installDIR())
    
    pisitools.rename("/usr/lib/libRmath.so","libRmath.so.0.0.0")
    pisitools.dosym("/usr/lib/libRmath.so.0.0.0","/usr/lib/libRmath.so.0")
    pisitools.dosym("/usr/lib/libRmath.so.0.0.0","/usr/lib/libRmath.so")



