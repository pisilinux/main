# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

#WorkDir = "boost-%s" % get.srcVERSION()

    
def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("boost_*", "boost-%s" % get.srcVERSION())
    
    shelltools.cd("boost-%s" % get.srcVERSION())
    
    shelltools.copytree("../boost-%s" % (get.srcVERSION().replace("_", "~")), "../boost-%s-36" % get.srcVERSION())
    
    shelltools.system("./bootstrap.sh --with-toolset=gcc --with-icu --with-python=/usr/bin/python2.7 --prefix=%s/usr" % get.installDIR())
    
    #shelltools.copytree("../boost-%s" % (get.srcVERSION().replace("_", "~")), "../boost-%s-36" % get.srcVERSION())
    shelltools.cd("../boost-%s-36" % get.srcVERSION())
    shelltools.system("sed -e '/using python/ s@;@: /usr/include/python${PYTHON_VERSION/3*/${PYTHON_VERSION}m} ;@' \
    -i bootstrap.sh")
    shelltools.system("./bootstrap.sh --with-toolset=gcc --with-icu --with-python=/usr/bin/python3.6 --prefix=%s/usr" % get.installDIR())
    
    shelltools.cd("..")
    
    
def build():
    shelltools.system("./b2 \
                       variant=release \
                       debug-symbols=off \
                       threading=multi \
                       runtime-link=shared \
                       link=shared,static \
                       toolset=gcc \
                       python=2.7 \
                       cflags=-fno-strict-aliasing \
                       --layout=system")
    
    shelltools.cd("../boost-%s-36" % get.srcVERSION())
    shelltools.system("./b2 \
                       variant=release \
                       debug-symbols=off \
                       threading=multi \
                       runtime-link=shared \
                       link=shared,static \
                       toolset=gcc \
                       python=3.6 \
                       cflags=-fno-strict-aliasing \
                       --layout=system")
    
    shelltools.cd("..")
    
def install():
    pisitools.dobin("b2")
    pisitools.dobin("bjam")
    shelltools.copytree("tools/boostbook/xsl", "%s/usr/share/boostbook/xsl" % get.installDIR())
    shelltools.copytree("tools/boostbook/dtd", "%s/usr/share/boostbook" % get.installDIR())
    shelltools.system("./b2 install threading=multi link=shared")
    
    shelltools.cd("../boost-%s-36" % get.srcVERSION())
    pisitools.dobin("b2")
    pisitools.dobin("bjam")
    shelltools.copytree("tools/boostbook/xsl", "%s/usr/share/boostbook/xsl" % get.installDIR())
    shelltools.copytree("tools/boostbook/dtd", "%s/usr/share/boostbook" % get.installDIR())
    shelltools.system("./b2 install threading=multi link=shared")
