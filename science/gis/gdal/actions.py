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
#    autotools.autoreconf("-vfi")
#    autotools.aclocal()
    pisitools.cflags.add("-fno-strict-aliasing")

    autotools.configure("--disable-static \
                         --enable-shared \
                         --datadir=/usr/share/gdal \
                         --with-ogdi \
                         --with-threads \
                         --with-jasper \
                         --with-odbc=/usr/lib/unixODBC \
                         --with-expat \
                         --with-cfitsio \
                         --with-hdf5 \
                         --with-netcdf \
                         --with-png \
                         --with-geos \
                         --without-mysql \
                         --with-curl \
                         --with-perl \
                         --with-jpeg \
                         --with-jpeg12=no \
                         --with-libtiff \
                         --with-sqlite3 \
                         --with-geotiff=external \
                         --with-podofo \
                         --with-spatialite \
                         --with-ogr \
                         --with-grib \
                         --with-curl \
                         --with-webp \
                         --with-python \
                         --without-poppler \
                         --with-xerces \
                         --with-openjpeg \
                         --without-libtool \
                         --without-hdf4 \
                         --without-fme \
                         --without-pcraster \
                         --without-kakadu \
                         --without-mrsid \
                         --without-jp2mrsid \
                         --without-msg \
                         --without-bsb \
                         --without-dods-root \
                         --without-oci \
                         --without-ingres \
                         --without-spatialite \
                         --without-dwgdirect \
                         --without-epsilon \
                         --without-idb \
                         --without-sde \
                         --mandir=/usr/share/man \
                         --without-ruby")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
    #for bug 13646
    #pisitools.dosed("GDALmake.opt", "PY_HAVE_SETUPTOOLS=1 ", "PY_HAVE_SETUPTOOLS= ")
    #pisitools.dosed("apps/GNUmakefile", "EXE_DEP_LIBS ", "KILL_EXE_DEP_LIBS ")
    


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #remove egg
#    pisitools.removeDir("/usr/lib/python2.7/site-packages/GDAL-*")

    #pisitools.domove("/usr/man/man3/*", "/usr/share/man/man3")
    #pisitools.removeDir("/usr/man/")
    #pisitools.domove("/usr/etc/bash_completion.d/*", "/etc/bash_completion.d")
    #pisitools.removeDir("/usr/etc")

    perlmodules.removePodfiles()
