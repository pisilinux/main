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
from pisi.actionsapi import python3modules, cmaketools


def setup():
    options_cfg = ''.join([
              '-DGDAL_USE_PNG=ON ',
              '-DGDAL_USE_CURL=ON ',
              '-DGDAL_USE_GEOS=ON ',
              '-DGDAL_USE_HDF5=ON ',
              '-DGDAL_USE_EXPAT=ON ',
              '-DGDAL_USE_MYSQL=ON ',
              '-DGDAL_USE_NETCDF=ON ',
              '-DGDAL_USE_GEOTIFF=ON ',
              '-DGDAL_USE_TIFF=ON ',
              '-DGDAL_USE_NETCDF=ON ',
              '-DGDAL_USE_SQLITE3=ON ',
              '-DGDAL_USE_OPENJPEG=ON ',
              '-DBUILD_PYTHON_BINDINGS=ON ',
              '-DGDAL_USE_SPATIALITE=ON'])
                  # '--with-perl ',
                  # '--enable-shared ',

    pisitools.cflags.add("-fno-strict-aliasing")
    cmaketools.configure("%s" % options_cfg)

    # fix unused direct dependency analysis
    # pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    cmaketools.make()
    # FIXME build man pages
    #autotools.make("man")
    
    # build python bindings
    # shelltools.cd("swig/python")
    # python3modules.compile()


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # install python bindings
    # shelltools.cd("swig/python")
    # python3modules.install()
    # shelltools.cd("../..")

    # perlmodules.removePodfiles()
    
    # fix rpath
    # shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/GDAL/Const/Const.so" % get.installDIR())
    # shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/GDAL/GDAL.so" % get.installDIR())
    # shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/GNM/GNM.so" % get.installDIR())
    # shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/OSR/OSR.so" % get.installDIR())
    # shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/OGR/OGR.so" % get.installDIR())
    
    pisitools.dodoc("LICENSE*")
