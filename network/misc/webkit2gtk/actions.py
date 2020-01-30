#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

paths = ["JavaScriptCore", "WebCore", "WebKit", "WebKit2"]
docs = ["AUTHORS", "COPYING.LIB", "THANKS", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    #shelltools.system("rm -r Source/ThirdParty/gtest/")
    cmaketools.configure("-DPORT=GTK \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIB_INSTALL_DIR=/usr/lib \
                          -DLIBEXEC_INSTALL_DIR=/usr/lib/webkit2gtk-4.0 \
                          -DENABLE_CREDENTIAL_STORAGE=ON \
                          -DENABLE_GEOLOCATION=ON \
                          -DENABLE_VIDEO=ON \
                          -DENABLE_WEB_AUDIO=ON \
                          -DENABLE_WEBGL=ON \
                          -DUSE_LIBHYPHEN=OFF \
                          -DUSE_WOFF2=OFF \
                          -DJPEG_INCLUDE_DIR=/usr/include/openjpeg-2.3 \
                          -DSHOULD_INSTALL_JS_SHELL=ON \
                          -DENABLE_MINIBROWSER=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS")
    shelltools.cd("Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                pisitools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))
