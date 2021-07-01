#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make("CXXFLAGS='%s' tbb_build_prefix=obj" % get.CXXFLAGS())

def install():
    shelltools.system("./install.sh %s" % get.installDIR())
    shelltools.system("cmake \
                        -DINSTALL_DIR='%s'/usr/lib/cmake/TBB \
                        -DSYSTEM_NAME=Linux \
                        -DTBB_VERSION_FILE='%s'/usr/include/tbb/tbb_stddef.h \
                        -P cmake/tbb_config_installer.cmake" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("README*")
