#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools


def setup():
    # shelltools.cd("%s" % get.workDIR())
    # shelltools.copytree("AppStream-%s" % get.srcVERSION(), "AppStream-qt6")

    # shelltools.cd("AppStream-%s" % get.srcVERSION())
    mesontools.configure("--libexecdir=lib \
                                        -Dstemming=false \
                                        -Dqt=true \
                                        -Dapidocs=false \
                                        -Dvapi=true")
    
    # shelltools.cd("../AppStream-qt6")
    # mesontools.configure("--libexecdir=lib \
                                        # -Dstemming=false \
                                        # -Dqt=true \
                                        # -Dapidocs=false \
                                        # -Dvapi=true")
   
def build():
    mesontools.build()

    # shelltools.cd("../AppStream-qt6")
    # mesontools.build()
    
def install():
    mesontools.install()

    # shelltools.cd("../AppStream-qt6")
    # mesontools.install()

    pisitools.insinto("/usr/share/pixmaps/", "docs/images/src/png/appstream-logo.png")
    
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README*")
