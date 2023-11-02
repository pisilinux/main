#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir="fftw-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")

    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-double" % get.srcVERSION())
    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-long-double" % get.srcVERSION())
    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-quad" % get.srcVERSION())
    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-cmake" % get.srcVERSION())

    autotools.configure("--enable-sse \
                         --enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --enable-threads \
                         --enable-mpi \
                         --enable-fortran \
                         --enable-single")

    shelltools.cd("../fftw-%s-quad" % get.srcVERSION())
    autotools.configure("--enable-quad-precision \
                         --enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --enable-fortran \
                         --enable-threads")

    # The only difference here is that there is no --enable-float
    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.configure("--enable-sse2 \
                         --enable-shared \
                         --disable-static \
                         --enable-fortran \
                         --disable-dependency-tracking \
                         --enable-threads")

    # The only difference here is --enable-long-double
    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.configure("--enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --enable-threads \
                         --enable-fortran \
                         --enable-long-double")

    shelltools.cd("../fftw-%s-cmake" % get.srcVERSION())
    shelltools.system("sed -e 's/3.6.9/3.6.10/' -i CMakeLists.txt")
    cmaketools.configure("-B build \
                                        -D CMAKE_INSTALL_PREFIX=/usr \
                                        -D CMAKE_BUILD_TYPE=None \
                                        -D ENABLE_OPENMP=ON \
                                        -D ENABLE_THREADS=ON \
                                        -D ENABLE_FLOAT=ON \
                                        -D ENABLE_LONG_DOUBLE=ON \
                                        -D ENABLE_QUAD_PRECISION=ON \
                                     ")
                                            # -D ENABLE_AVX2=ON \
                                            # -D ENABLE_AVX=ON \
                                            # -D ENABLE_SSE=ON  \
                                            # -D ENABLE_SSE2=ON \

#def check():
    #autotools.make("check")

    #shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    #autotools.make("check")

    #shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    #autotools.make("check")

    #shelltools.cd("../fftw-%s-quad" % get.srcVERSION())
    #autotools.make("check")

def build():
    autotools.make()

    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.make()

    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.make()

    shelltools.cd("../fftw-%s-quad" % get.srcVERSION())
    autotools.make()

    shelltools.cd("../fftw-%s-cmake" % get.srcVERSION())
    shelltools.system("export F77='gfortran'")
    shelltools.export("CFLAGS", " -O3 -fomit-frame-pointer -malign-double -fstrict-aliasing -ffast-math")
    shelltools.cd("build")
    cmaketools.make()

    # shelltools.cd("../fftw-%s-cmake" % get.srcVERSION())
    shelltools.system("""sed -e 's|\(IMPORTED_LOCATION_NONE\).*|\1 "/usr/lib/libfftw3.so.3"|' -i FFTW3LibraryDepends.cmake""")

def install():
    # shelltools.cd("../fftw-%s" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-quad" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s" % get.srcVERSION())

    shelltools.cd("../fftw-%s-cmake" % get.srcVERSION())
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/lib/cmake/fftw3", "FFTW3LibraryDepends.cmake")

    pisitools.dohtml("../doc/html/*")
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO", "CONVENTIONS")
