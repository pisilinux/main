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
from pisi.actionsapi import pythonmodules


def setup():
    options_cfg = ''.join([
              '--with-png ',
              '--with-curl ',
              '--with-geos ',
              '--with-hdf5 ',
              '--with-perl ',
              '--with-expat ',
              '--with-mysql ',
              '--with-netcdf ',
              '--with-geotiff ',
              '--with-libtiff ',
              '--with-sqlite3 ',
              '--enable-shared ',
              '--with-openjpeg ',
              '--with-spatialite'])

    pisitools.cflags.add("-fno-strict-aliasing")
    autotools.configure("%s" % options_cfg)

    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()
    # FIXME build man pages
    #autotools.make("man")
    
    # build python bindings
    shelltools.cd("swig/python")
    pythonmodules.compile()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # install python bindings
    shelltools.cd("swig/python")
    pythonmodules.install()
    shelltools.cd("../..")

    perlmodules.removePodfiles()
    
    # fix rpath
    shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/GDAL/Const/Const.so" % get.installDIR())
    shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/GDAL/GDAL.so" % get.installDIR())
    shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/GNM/GNM.so" % get.installDIR())
    shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/OSR/OSR.so" % get.installDIR())
    shelltools.system("chrpath -d %s/usr/lib/perl5/x86_64-linux-thread-multi/auto/Geo/OGR/OGR.so" % get.installDIR())
    
    pisitools.dodoc("LICENSE*")
