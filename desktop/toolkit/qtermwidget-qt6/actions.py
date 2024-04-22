# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    # pisitools.dosed("CMakeLists.txt", "0.13.0", "2.0.0")
    # pisitools.dosed("CMakeLists.txt", "lxqt-build-toolsConfig.cmake", "lxqt2-build-tools-config.cmake")
    # pisitools.dosed("CMakeLists.txt", "lxqt-build-tools-config.cmake", "lxqt2-build-tools-config-version.cmake")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_PREFIX_PATH=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DUSE_QT6=ON \
                          -DCMAKE_INSTALL_LIBDIR=lib", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("LICENSE", "AUTHORS", "README.md", "CHANGELOG")
