#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's@ca-bundle.pem@ca-bundle.crt@' CMakeLists.txt")
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_TESTS=OFF \
                          -DQCA_INSTALL_IN_QT_PREFIX=ON \
                          -DQCA_MAN_INSTALL_DIR=/usr/share/man \
                          -DOPENSSL_INCLUDE_DIR=/usr/include/openssl \
                          -DOPENSSL_SSL_LIBRARY=/usr/lib/libssl.so \
                          -DQT6=ON \
                          -DQCA_SUFFIX=qt6 \
                          -DOPENSSL_CRYPTO_LIBRARY=/usr/lib/libcrypto.so", sourceDir="..")
 

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s" % bin)

    shelltools.cd("..")
    pisitools.dodoc("README", "TODO", "COPYING")
    
    #pisitools.domove("/usr/share/qt5/man/man1/qcatool-qt5.1", "/usr/share/man/man1/qcatool-qt5.1")
    #pisitools.removeDir("/usr/share/qt5")
