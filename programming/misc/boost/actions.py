# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("boost_*", "boost-%s" % get.srcVERSION())
    
    shelltools.cd("boost-%s" % get.srcVERSION())
    
    shelltools.system("./bootstrap.sh --with-toolset=gcc \
                                      --with-icu \
                                      --with-python=python3 \
                                      --prefix=%s/usr" % get.installDIR())

    shelltools.system('echo "using mpi ;" >> project-config.jam')

    shelltools.cd("tools/build")
    shelltools.system("./bootstrap.sh --with-toolset --prefix=%s/usr" % get.installDIR())

    shelltools.cd("..")

def build():
    shelltools.system("./b2 stage \
                       variant=release \
                       debug-symbols=off \
                       threading=multi \
                       runtime-link=shared \
                       link=shared,static \
                       toolset=gcc \
                       python=3.11 \
                       cflags='-fno-strict-aliasing -Wno-unused-local-typedefs -Wno-maybe-uninitialized -Wno-deprecated-declarations' \
                       cxxflags='-fno-strict-aliasing -Wno-unused-local-typedefs -Wno-maybe-uninitialized -Wno-deprecated-declarations' \
                       --layout=system \
                       --with-mpi")

def install():
    pisitools.dobin("b2")
    # pisitools.dobin("tools/build/src/engine/bjam")
    pisitools.dosym("/usr/bin/b2", "/usr/bin/bjam")
    shelltools.copytree("tools/boostbook/xsl", "%s/usr/share/boostbook/xsl" % get.installDIR())
    shelltools.copytree("tools/boostbook/dtd", "%s/usr/share/boostbook" % get.installDIR())


    shelltools.system("./b2 install threading=multi link=shared")

    shelltools.cd("tools/build")
    shelltools.system("./b2 install")
    shelltools.cd("..")
    
    # some packages need this library as : libboost_python3.so
    pisitools.dosym("/usr/lib/libboost_python311.so.1.87.0", "/usr/lib/libboost_python3.so")

    shelltools.touch("__init__.py")
    pisitools.insinto("/usr/lib/python3.11/site-packages/openmpi/boost", "__init__.py")

    pisitools.domove("/usr/lib/boost-python3.11/mpi.so", "/usr/lib/python3.11/site-packages/boost/")

    pisitools.removeDir("/usr/lib/boost-python3.11")
